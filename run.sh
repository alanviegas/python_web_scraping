#docker-compose up -d --build
docker-compose up -d

docker-compose logs -f -t api_pipeline api_persistenciadados api_consultareclameaqui 
#docker-compose logs -f -t api_pipeline

docker-compose ps
