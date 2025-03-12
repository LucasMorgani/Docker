# Definindo a imagem a ser utilizada no Dockerfile
FROM alpine:3.21.3

# adduser           Adicionando um usuário..
    # -h /var/testeapp  Definindo qual será o seu diretório home
    # -s /bin/sh        Definindo qual será seu shell
    # -D                Definindo que o usuário NÃO terá uma senha
    # testeapp          Definindo o nome do usuário a ser criado
RUN adduser -h /var/testeapp -s /bin/sh -D testeapp

# Definindo o diretório principal como /var/testeapp
    # Aqui o WORKDIR está servindo apenas para mudar de diretório
WORKDIR /var/testeapp

# Instalando o git e clonando um repositório dentro dele
RUN apk add --no-cache git \
    && git clone https://github.com/LucasMorgani/Shell-Script.git


# Alternando para o WORKDIR real
WORKDIR /var/testeapp/Shell-Script/banco_de_dados
    
# Instalando o dialog
RUN apk add --no-cache dialog 

# Alterando o owner dos arquivos que serão necessários 
RUN chown testeapp:testeapp sistema_de_usuarios.sh banco_de_dados.txt

# alternando para o usuário testeapp
USER testeapp

# Rodando a aplicação assim que acessar via terminal interativo
CMD [ "sh", "sistema_de_usuarios.sh" ]