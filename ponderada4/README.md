# Logging

**Enunciado**: [aqui](https://murilo-zc.github.io/M10-Inteli-Eng-Comp/Encontros/encontro_10/atividade_ponderada/)

**Repositório base**: [Murilo-ZC/M10-Inteli-Eng-Comp](https://github.com/Murilo-ZC/M10-Inteli-Eng-Comp/tree/main/src/encontro11/sistema03)

---

Em cima do repositório base, que já estava com Kibana, ElasticSearch e FileBeat configurados e um servidor FastAPI rodando, eu:

- Criei um novo servidor em Go, na pasta `gin`,  com um CRUD básico de usuário.
- Configurei o logger do gin para escrever no arquivo `logs/gin_app.log`.
- Adicionei o gin no docker-compose, fazendo o bind das pasta de logs com a minha máquina
- Adicionei um nginx no docker-compose, que faz um gateway para ambos os servidores
- Também fiz o binding da pasta `/var/logs/nginx` de dentro do container Nginx para minha máquina
- Configurei o FileBeat para separar os logs entre os serviços `fastapi, gin` e `nginx`, pelo nome do arquivo de logs
- Resumidamente, é isso! :)

## Como executar:

- na raíz do repositório, rode `docker compose up` e acesse `http://localhost:5601` para explorar seus logs :) 
