from fastapi import FastAPI, Depends, HTTPException, status, Request, Response
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import JSONResponse, StreamingResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import delete
from models import User, Task
import models
import database
import auth
from pydantic import BaseModel
import pyppeteer
import io

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class TaskCreate(BaseModel):
    title: str

class UserCreate(BaseModel):
    username: str
    password: str

@app.post("/api/token")
async def login_for_access_token(request: Request, db: AsyncSession = Depends(database.get_db)):
    form_data = await request.json()
    user = await auth.authenticate_user(form_data["username"], form_data["password"], db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/api/register", response_model=UserCreate)
async def register_user(request: Request, db: AsyncSession = Depends(database.get_db)):
    user_data = await request.json()
    user = models.User(username=user_data["username"], password=user_data["password"])
    async with db as session:
        session.add(user)
        await session.commit()
    return {"message": "User created successfully", "username": user_data["username"], "password": user_data["password"]}

@app.post("/api/login")
async def login(request: Request, db: AsyncSession = Depends(database.get_db)):
    form_data = await request.json()
    user = await auth.authenticate_user(form_data["username"], form_data["password"], db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth.create_access_token(user.id)
    response = JSONResponse(content={"message": "User logged in successfully"})
    response.set_cookie(key="jwt_token", value=access_token)
    return response

@app.get("/api/tasks/")
async def read_tasks(request: Request, skip: int = 0, limit: int = 100, db: AsyncSession = Depends(database.get_db)):
    token = request.cookies.get("jwt_token")
    if not token:
        raise HTTPException(status_code=401, detail="JWT token is required")

    user = await auth.get_current_user(token, db)
    if not user:
        raise HTTPException(status_code=401, detail="User authentication failed")

    async with db:
        result = await db.execute(select(Task).where(Task.owner_id == user.id).offset(skip).limit(limit))
        tasks = result.scalars().all()

    tasks_data = [task.dict() for task in tasks]
    return JSONResponse(content={"tasks": tasks_data})

@app.post("/api/tasks/")
async def create_task(request: Request, task: TaskCreate, db: AsyncSession = Depends(database.get_db)):
    token = request.cookies.get("jwt_token")
    if not token:
        raise HTTPException(status_code=401, detail="No JWT token found in cookies")

    user = await auth.get_current_user(token, db)
    if not user:
        raise HTTPException(status_code=401, detail="User authentication failed")

    new_task = Task(title=task.title, owner_id=user.id)

    async with db:
        db.add(new_task)
        await db.commit()
        await db.refresh(new_task)

    return {"id": new_task.id, "title": new_task.title, "completed": new_task.completed, "owner_id": new_task.owner_id}

@app.delete("/api/tasks/{task_id}")
async def delete_task(task_id: int, request: Request, db: AsyncSession = Depends(database.get_db)):

    token = request.cookies.get("jwt_token")
    if not token:
        raise HTTPException(status_code=401, detail="Authentication credentials were not provided.")

    user = await auth.get_current_user(token, db)
    if not user:
        raise HTTPException(status_code=401, detail="User could not be authenticated.")

    async with db:
        result = await db.execute(delete(models.Task).where(
            models.Task.id == task_id,
            models.Task.owner_id == user.id
        ))
        await db.commit()

        if result.rowcount == 0:
            raise HTTPException(status_code=404, detail="Task not found or not owned by the user")
        
        return {"message": "Task deleted successfully"}

@app.put("/api/task/{task_id}/complete")
async def complete_task(task_id: int, request: Request, db: AsyncSession = Depends(database.get_db)):
    token = request.cookies.get("jwt_token")
    if not token:
        raise HTTPException(status_code=401, detail="Authentication credentials were not provided.")

    user = await auth.get_current_user(token, db)
    if not user:
        raise HTTPException(status_code=401, detail="User could not be authenticated.")
    
    async with db:
        result = await db.execute(select(models.Task).where(
            models.Task.id == task_id,
            models.Task.owner_id == user.id
        ))
        task = result.scalars().first()
        
        if not task:
            raise HTTPException(status_code=404, detail="Task not found or not owned by the user")
        
        task.completed = True
        await db.commit()

        return {"message": "Task completed successfully"}

@app.post("/api/screenshot")
async def capture_screenshot(request: Request):
    data = await request.json()
    url = data.get("url")
    if not url:
        raise HTTPException(status_code=400, detail="URL is required")
    
    try:
        browser = await pyppeteer.launch(headless=True)
        page = await browser.newPage()
        await page.goto(url)
        screenshot = await page.screenshot()
        await browser.close()

        return StreamingResponse(io.BytesIO(screenshot), media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

@app.on_event("startup")
async def startup_event():
    await models.create_tables()
