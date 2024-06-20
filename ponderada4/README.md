# Ponderada 4

Em cima do repositório base que já possuía uma configuração inicial com Kibana, ElasticSearch e FileBeat, além de um servidor FastAPI em funcionamento, realizei uma série de ajustes e adições para expandir a aplicação. Aqui estão os passos principais que foram realizados:

**1. Desenvolvimento do Servidor em Go com Gin:** Criei um novo servidor em Go na pasta gin, implementando um CRUD básico de usuário utilizando o framework Gin.

**2. Configuração do Logger do Gin:** Configurei o logger do Gin para que os registros fossem escritos no arquivo logs/gin_app.log, facilitando o monitoramento e debug da aplicação.

**3. Integração do Gin no Docker Compose:** Adicionei o serviço do Gin ao docker-compose.yml, garantindo que o container fosse executado em conjunto com os outros serviços. Além disso, configurei o bind das pastas de logs para que fossem acessíveis na minha máquina local.

**4. Inclusão do Nginx no Docker Compose:** Integrei um servidor Nginx ao docker-compose.yml para atuar como um gateway para os serviços FastAPI e Gin. Isso proporciona um ponto de entrada único para a aplicação.

**5. Configuração de Logs do Nginx:** Realizei o bind da pasta /var/logs/nginx do container Nginx para a minha máquina local, permitindo o acesso aos logs de Nginx para monitoramento e análise.

**6. Configuração do FileBeat:** Ajustei a configuração do FileBeat para separar e enviar os logs dos serviços fastapi, gin e nginx para o ElasticSearch, utilizando o nome do arquivo de logs como critério de separação. Isso simplifica a organização e análise dos registros de cada serviço.

## Como executar?

Para testar a implementação é necessário entrar na raiz do repositório:

```
docker compose up
```

Por conseguinte, acesse `http://localhost:5601` para explorar seus logs.

## Demonstração 
O vídeo de demonstração está na pasta `/demonstracao`
