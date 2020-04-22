#docker-compose up -d --build
docker-compose up -d

#docker-compose logs -f -t api_consultareclameaqui api_consultareclameaqui 
docker-compose logs -f -t api_persistenciadados mongodb

docker-compose ps
