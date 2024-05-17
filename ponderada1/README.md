# Ponderada 1

A atividade envolve a implementação de dois servidores para o gerenciamento de tarefas:

1. síncrono utilizando Flask
2. assíncrono utilizando FastAPI

Cada servidor funciona de forma independente em um ambiente Dockerizado dedicado, utilizando uma instância exclusiva do Postgres para armazenamento de dados. Ambas as aplicações fornecem recursos completos de autenticação de usuários por meio de tokens JWT, os quais são armazenados de forma segura em cookies. Além disso, possibilitam a gestão completa de tarefas, incluindo sua criação, atualização e remoção.


nivel 0 ao 3 - flask 


## Como executar?

Para testar a implementação assíncrona é necessário entrar na pasta `/fast` e executar o comando:

```
docker compose up
```

Seguindo o mesmo raciocínio, para rodar a implementação assíncrona entre na pasta `/flask` e execute o comando:

```
docker compose up
```

Por fim, para testar o teste de escalabilidade, responsável por comparar o desempenho dos dois servidores em condições de carga simultânea, é necessário rodar:

```
python3 test.py
``` 

## Demonstração 
O vídeo de demonstração está na pasta `/demonstracao`
