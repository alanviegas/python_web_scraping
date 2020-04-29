#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Date: 20190506
User: Alan Viegas
Project: WebScrap ReclameAqui
'''

import requests

def get_reclameaqui(metod, company, collection):

    url = 'http://api_consultareclameaqui:5000/{}'.format(collection)
    params = {}
    params['company'] = company 
    
    print('DEBUG GET 1: {}'.format(url)) 
    print('DEBUG GET 2: {}'.format(params))
    
    if metod == 'GET':
        response = requests.get(url, params=params)
       
    print(response.status_code)
    print(response.text)

    return response
