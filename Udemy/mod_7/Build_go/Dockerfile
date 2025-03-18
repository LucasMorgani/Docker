

#----------------------- First stage: build
# Puxando a imagem do golang
# As builder    Está defindo um nome para o estágio: builder
FROM golang:1.24.1-bullseye AS builder
# Mudando o diretório principal para /app
WORKDIR /app
# Copiando a aplicação para dentro do container
COPY app.go .
# Executando a aplicação e criando um "main" dela
RUN go mod init main && \
  CGO_ENABLED=0 go build
#--------------------------------------------




#----------------------- Second stage: Final
# Puxando a imagem "scratch" (imagem crua do linux, apenas para executar bin)
FROM scratch
# Expondo a porta 80
EXPOSE 80
# Copiando as pastas /app/main e /go/main para a imagem reduzida
COPY --from=builder /app/main /go/main
# Executando o comando de execussão do programa
CMD [ "/go/main" ]
#--------------------------------------------