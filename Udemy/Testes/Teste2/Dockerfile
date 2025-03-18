# Imagem a ser utilizada
FROM node:23-alpine3.20

# Criando um diretório de trabalho
WORKDIR /app

RUN apk add --no-cache git \
    && git clone --mirror https://github.com/LucasMorgani/nodeJS-Alura.git \
    && 