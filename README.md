# SmartVit-Support-Service
SmartVit é um software destinado ao controle de culturas de uva com destino comercial para consumo. Portanto esse repositório é dedicado ao microservice do support.

## Rodar Ambiente
    sudo docker-compose build
    sudo docker-compose up

## Rodar Testes
    docker exec -it CONTAINER_ID pytest

## Rodar Bash do Mongodb
    docker exec -it CONTAINER_ID bash

## Comandos Úteis

* Listar containers dockers
  * docker ps -a
* Listar imagens dockers
  * docker ps
* Parar todos os containers
  * docker stop $(docker ps -a -q)
* Apagar todos os containers
  * docker rm $(docker ps -a -q)
* Entrar no admin do mongodb
  * mongo admin --username YOURUSERNAME --password YOURPASSWORD