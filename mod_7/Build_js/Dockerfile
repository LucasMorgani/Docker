# Pegando uma imagem base do node
FROM node:23-alpine3.20     

# Definindo quem é o mantenedor a fins de organização
LABEL maintainer="Lucas Morgani"    

# Testando a "saúde" do container
# Caso o curl no localhost dê um erro, saia com exit 1. Isso o definirá como "unhealth"
HEALTHCHECK CMD curl -sf http://localhost:3000/ || exit 1

# Criando um volume
# Esse volume terá como source uma pasta criada na máquina host
VOLUME [ "/var/nodeapp" ]

# Executar esses comandos..
# adduser               Adicionar usuário
# -h /var/nodeapp       Mudar a home para /var/nodeapp
# -s /bin/bash          Conceder acesso ao shell /bin/bash
# -D                    Não ser necessário senha
# nodeapp               Nome do usuário
# && apk add curl       Adicionando o curl na imagem, para que possa ser feito o healthcheck
RUN adduser -h /var/nodeapp -s /bin/bash -D nodeapp && apk add curl

# O WORKDIR serve para mudar de diretório assim que acessar o container
WORKDIR /var/nodeapp           

# Copiar do host, o app.js para o diretório atual (/var/node)
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
