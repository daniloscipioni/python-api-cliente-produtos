# Visão Geral do Projeto

Este projeto foi criado em python com a lib FastApi que visar promover dados de clientes para visualização, alteração, remoção e edição, 
assim como seus produtos favoritos que são gerenciados por uma api externa mas validados na integração.

Este projeto faz o acesso a um banco de dados postgres no qual faz a persistencia de dados de clientes e favoritos que são relacionados por um campo em comum
que é o id do usuario.


## Pre requisitos

Antes de executar o projeto, é necessario ter:

* Python 3.11 ou mais recente
* Docker para conteinizar o postgresSql ou o postgresSql instalado localmente


## Docker

Caso tenha o docker instalado executar comando a seguir na raiz do projeto

`docker compose -f postgresql-compose.yml up -d`

## Variaveis de ambiente

Criar um arquivo .env na raiz do projeto e incluir a variavel substituindo <usuario> e <senha>
pelos valores de acesso ao banco de dados.
Caso tenha utilizado o docker, os valores são
usuario = admin e senha = admin

POSTGRES_URL=postgresql://usuario:senha@localhost:5432/postgres

## Migrations

Rodar o comando a seguir na raiz do projeto para criar as tabelas no banco de dados

`python .\src\database\database_start.py`

Esse comando vai remover e criar todas as tabelas do projeto

## Banco de dados

O Banco de dados possui 2 tabelas (tbl_cliente e tbl_favoritos) com relacionamento de 1 para n, onde 1 cliente pode ter 1 ou mais
favoritos cadastrados

![banco_dados.PNG](environment/banco_dados.PNG)

## Execução do projeto


1. Instalar as dependencias do python

`pip install -r requirements.txt`


2. Iniciar o servidor

Rodar o projeto com seguinte comando na raiz do projeto:

`fastapi dev main.py`

Isso irá subir um servidor no endereco http://127.0.0.1:8000.


3. Acessar a documentação

Assim que o serviço for iniciado é possivel acessar a documentação atraves dos links:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc