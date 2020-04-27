# Objetivo
 
    Estudo para fazer uma web scraping no site ReclameAqui para pegar as quantidades de reclamações de uma 
    determinada empresa e armazenar o resultado em um banco de dados.

## Tecnologias e Bibliotecas utilizadas
 
 - Python 3.6
    - BeautifulSoup
    - Flask
    - Jsonschema
    - Pymongo
    - Selenium 
 - Mongo 3.6
 - Docker / Docker Composer
 - Apache Airflow

## Estrutura do pastas do projeto
 
 - "/app/API_consultaReclameAqui" : API que consulta o site ReclameAqui e retorna os resultados
    - "log" : Logs da API
    - "src" : Arquivos fontes da API
        - "dao" : Camada de acesso aos dados - Scraping com Selenium e BeautifulSoup
        - "service" : Camada de serviços - REST API de consultas ao ReclameAqui com Flask
    - "test" : Arquivos de testes da API
    - "utils" : Utilitários e ferramentas utilizadas no projeto
    - "app.sh" : ShellScript que inicializa a API
    - "Dockerfile" : Definições específicas do Docker

 - "/app/API_persistenciaDados" : API que persiste os dados no MongoDB
    - "log" : Logs da API
    - "src" : Arquivos fontes da API
        - "dao" : Camada de acesso aos dados - Modelo de dados e armazenamento no MongoDB com Pymongo
        - "service" : Camada de serviços - REST API de CRUD (Create, Read, Update and Delete) com Flask
    - "test" : Arquivos de testes da API
    - "utils" : Utilitários e ferramentas utilizadas no projeto
    - "mongodb" : Datafiles do MongoDB
    - "app.sh" : ShellScript que inicializa a API
    - "Dockerfile" : Definições específicas do Docker

 - "/app/Airflow_pipeline" : Workflow que irá orquestrar o pipeline

 - "/docs" : Documentos e arquivos do projeto
 
 - "docker-compose.yml" : Definições para subir os containers
 - "run.sh" : ShellScript que sobe todos os ambientes

## Releases
    - v101
        - Deploy Inicial

## Commits

## Futuras Melhorias
 - Implemntar autenticação com JWT nas APIs