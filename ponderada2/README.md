# Ponderada 2

A atividade envolve a criação de um aplicativo de uma lista de tarefas com um **backend dockerizado** e uma **interface mobile feita com Flutter**.

Dessa maneira, a API (desenvolvida na ponderada), assíncrona utilizando Fast API, tem como única responsabilidade gerenciar uma tabela de tasks. Por outro lado, a interface em flutter tem uma página home e uma com as listas de tarefas.

## Como executar?

Para testar a implementação assíncrona é necessário entrar na pasta `/fast` e executar o comando:

```
docker compose up
```

Por conseguinte, para rodar a aplicação em flutter (com o Android Studio já instalado), entre na pasta `/mobile/todoapp/lib` e com o emulador configurado para Android, execute o comando:

```
main.dart <!-- NO EMULADOR -->
```

## Demonstração 
O vídeo de demonstração está na pasta `/demonstracao`
