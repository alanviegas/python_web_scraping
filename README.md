# Objetivo

    Estudo para fazer uma web scraping no site ReclameAqui para pegar as quantidades de reclamações de uma 
    determinada empresa e armazenar o resultado em um banco de dados.

## Passo a passo

 - Em uma pasta qualquer baixe o projeto:
        git clone https://github.com/alanviegas/python_web_scraping.git
        cd python_web_scraping

 - Execute o run.sh para criar os containers do Docker e subir os serviços.
        ./run.sh

 - Para acessar a pagina de adminstração do AirFlow acessar a seguinte URL: 
        http://localhost:8080/admin/

 - Haverá os seguintes jobs criados:
        1) scraping_and_persist_scores (job ok: "scraping_and_persist_scores - evidencia de testes.pdf")
        Faz o webscraping no site ReclameAqui e armazena no MongoDB os scores gerais de reclamações,
        com as seguintes informações:
            reclamations: Total de reclamações 
            answered: Total de reclamações respondidas 
            unanswered: Total de reclamações não respondidas
            response_time: Tempo medio de resposta das reclamações respondidas
        2) scraping_and_persist_reclamations (este job possui um Bug)
        Faz o webscraping no site ReclameAqui e armazena no MongoDB as 10 reclamações mais recentes, 
        com as seguintes informações:
            title: Título da reclamação
            locale_date: Local e Data
            description: Descrição da reclamação
        3) query_and_export_reclamations (a desenvolver)
        Faz a consulta no MongoDB e gera um arquivo CSV de todas as reclamações armazenadas no banco de dados,
        com as seguintes informações:
            title: Título da reclamação
            locale_date: Local e Data
            description: Descrição da reclamação
 
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
    git push https://github.com/alanviegas/python_web_scraping.git
 - "docker-compose.yml" : Definições para subir os containers
 - "run.sh" : ShellScript que sobe todos os ambientes

## Releases
 
 - v0
    - Deploy Inicial

## Tecnologias e Bibliotecas utilizadas
 
 - Python 3.6
    - BeautifulSoup
    - Flask
    - Jsonschema
    - Pymongo
    - Selenium 
 - Mongo 3.6
 - Docker / Docker Composer 1.18
 - Apache Airflow

## Backlogs
 - Implementar autenticação com JWT nas APIs para garantir segurança
 - Implementar no Airflow o job query_and_export_reclamations

## Bugs
 - O job scraping_and_persist_reclamations não esta conseguindo fazer o scraping das 10 reclamações mais recentes,
   parecer ser algum problema na formatação do json.

