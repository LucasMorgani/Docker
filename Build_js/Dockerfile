# Pegando uma imagem base do node
FROM node:23-alpine3.20     

# Definindo quem é o mantenedor a fins de organização
LABEL maintainer="Lucas Morgani"    

# Executar esses comandos..
# adduser               Adicionar usuário
# -h /var/nodeapp       Mudar a home para /var/nodeapp
# -s /bin/bash          Conceder acesso ao shell /bin/bash
# -D                    Não ser necessário senha
# nodeapp               Nome do usuário
RUN adduser -h /var/nodeapp -s /bin/bash -D nodeapp

# O WORKDIR serve para mudar de diretório assim que acessar o container
WORKDIR /var/nodeapp           

# Copiar do host, o appv2.js para o diretório atual (/var/node)
COPY app.js .

# Alterando o owner do arquivo app.js para o user nodeapp
RUN chown nodeapp:nodeapp app.js

# Exportando a porta
EXPOSE 3000         

# Colocando a possibilidade de passar um argumento chamado VERSION na hora da build
ARG VERSION             
# Caso seja informado, criará uma variável ambiente no valor passado para o ARG
# caso seja nulo, o valor atribuido será 1.0.0
ENV VERSION=${VERSION:-1.0.0}

# Alterando para o usuário nodeapp
USER nodeapp

# Executando o comando node app.js
CMD [ "node", "app.js" ]
