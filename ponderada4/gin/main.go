package main

import (
    "github.com/gin-gonic/gin"
    "net/http"
    "strconv"
	"os"
	"log"
)

type User struct {
    ID    int    `json:"id"`
    Name  string `json:"name"`
    Email string `json:"email"`
}

var users = []User{
    {ID: 1, Name: "John Doe", Email: "john@example.com"},
    {ID: 2, Name: "Jane Doe", Email: "jane@example.com"},
}

var nextID = 3

func main() {
    r := gin.Default()

    // Create log file
    f, err := os.OpenFile("/logs/gin_app.log", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
    if err != nil {
        log.Fatal(err)
    }
    gin.DefaultWriter = f

    // Middleware to log requests
    r.Use(gin.Logger())

    r.GET("/users", getUsers)
    r.GET("/users/:id", getUserByID)
    r.POST("/users", createUser)
    r.PUT("/users/:id", updateUser)
    r.DELETE("/users/:id", deleteUser)

    r.Run(":8080")
}

func getUsers(c *gin.Context) {
    c.JSON(http.StatusOK, users)
}

func getUserByID(c *gin.Context) {
    id, _ := strconv.Atoi(c.Param("id"))
    for _, user := range users {
        if user.ID == id {
            c.JSON(http.StatusOK, user)
            return
        }
    }
    c.JSON(http.StatusNotFound, gin.H{"message": "user not found"})
}

func createUser(c *gin.Context) {
    var newUser User
    if err := c.BindJSON(&newUser); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    newUser.ID = nextID
    nextID++
    users = append(users, newUser)
    c.JSON(http.StatusCreated, newUser)
}

func updateUser(c *gin.Context) {
    id, _ := strconv.Atoi(c.Param("id"))
    var updatedUser User
    if err := c.BindJSON(&updatedUser); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
        return
    }
    for i, user := range users {
        if user.ID == id {
            users[i] = updatedUser
            users[i].ID = id
            c.JSON(http.StatusOK, users[i])
            return
        }
    }
    c.JSON(http.StatusNotFound, gin.H{"message": "user not found"})
}

func deleteUser(c *gin.Context) {
    id, _ := strconv.Atoi(c.Param("id"))
    for i, user := range users {
        if user.ID == id {
            users = append(users[:i], users[i+1:]...)
            c.JSON(http.StatusOK, gin.H{"message": "user deleted"})
            return
        }
    }
    c.JSON(http.StatusNotFound, gin.H{"message": "user not found"})
}
