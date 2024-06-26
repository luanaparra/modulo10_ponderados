# Ponderada 3

Nessa ponderada foi implementada: 
1. Aplicativo Flutter com tela de login (sem autenticação de rotas, necessáriamente), cadastro de usuário e tela para captura de imagens.
2. Backend em Microsserviços que realiza o cadastro de usuários e faz o log das ações que o usuário realiza no aplicativo (por hora só login e criação de conta).
3. Aplicativo Flutter enviando as imagens para o processamento;
4. Backend em Microsserviços que recebe as imagens e as processa, retornando o resultado para o aplicativo;
5. Backend em Microsserviços que realiza o log das ações que o usuário realiza no aplicativo (por hora só login, criação de conta e envio de imagens);
6. Serviço de notificação que envia uma notificação para o usuário quando o processamento da imagem termina.

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
