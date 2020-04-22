#docker-compose up -d --build
docker-compose up -d

docker-compose logs -f -t mongodb api_persistenciadados api_consultareclameaqui 

docker-compose ps
