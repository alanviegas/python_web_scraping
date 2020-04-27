'''
Date: 20190506
User: Semantix
Project: Template for Unit test
'''

import pytest
import requests
import json


###############Scores########################
#Teste POST
# headers = {'content-type': 'application/json'}
# url = 'http://localhost:5005/scores/'
# data = {"answered": "6666", 
# 		"reclamations": "6151", 
#         "response_time": "15 dias e 21 horas ", 
#         "unanswered": "113"
#         }
# params = {'company': 'Cielo', 'date': '20190421'}
# response = requests.post(url, params=params, data=json.dumps(data), headers=headers)
# print(response.status_code)
# print(response.text)

# #Teste GET
# url = 'http://localhost:5005/scores/'
# params = {'company': 'Cielo'}
# response = requests.get(url, params=params)
# print(response.status_code)
# print(response.text)


# # Teste DELETE (company and date)
# url = 'http://localhost:5005/scores/'
# params = {'company': 'Cielo', 'date': '20190101'}
# response = requests.delete(url, params=params)
# print(response.status_code)
# print(response.text)

# Teste DELETE (company)
# url = 'http://localhost:5005/scores/'
# params = {'company': 'Cielo'}
# response = requests.delete(url, params=params)
# print(response.status_code)
# print(response.text)



##############################Reclamations####################
#Teste POST
# headers = {'content-type': 'application/json'}
# url = 'http://localhost:5005/reclamations/'
# data=open('/home/alanviegas/Documentos/estudos/desafioSemantix/apps/API_persistenciaDados/test/reclamations.json', 'rb').read()
# params = {'company': 'Cielo', 'date': '20200421'}
# response = requests.post(url, params=params, data=data, headers=headers)
# print(response.status_code)
# print(response.text)


# #Teste GET (company)
# url = 'http://localhost:5005/reclamations/'
# params = {'company': 'Cielo'}
# response = requests.get(url, params=params)
# print(response.status_code)
# print(response.text)


# #Teste GET (company and date)
# url = 'http://localhost:5005/reclamations/'
# params = {'company': 'Cielo','date': '20200421'}
# response = requests.get(url, params=params)
# print(response.status_code)
# print(response.text)


# # Teste DELETE (company and date)
# url = 'http://localhost:5005/reclamations/'
# params = {'company': 'Cielo', 'date': '20200421'}
# response = requests.delete(url, params=params)
# print(response.status_code)
# print(response.text)


# Teste DELETE (company)
# url = 'http://localhost:5005/reclamations/'
# params = {'company': 'Cielo'}
# response = requests.delete(url, params=params)
# print(response.status_code)
# print(response.text)
