FROM golang:alpine

RUN go install github.com/air-verse/air@latest

WORKDIR /app

ENTRYPOINT ["air"]