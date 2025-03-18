# Definindo a imagem base
FROM node:23-alpine3.20

# Definindo o diretório de trabalho
WORKDIR /app-node

# Abrindo uma variavel chamada PORT_BUILD (essa variavel só existe durante a criação do container)
ARG PORT_BUILD=6000
# Definindo uma variável de ambiente chamada PORT. A aplicação acessará as variaveis de ambiente do -
# - SO (container) e receberá o valor definido
ENV PORT=$PORT_BUILD


# Expondo a aplicação na porta 3000
EXPOSE $PORT_BUILD

# Copiando os arquivos do diretório atual para o diretorio atual do container
COPY . .

# Instalando
RUN npm install

# Executando o npm start como entrypoint
ENTRYPOINT npm start