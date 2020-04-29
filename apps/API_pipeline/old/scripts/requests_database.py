#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Date: 20190506
User: Alan Viegas
Project: WebScrap ReclameAqui
'''

import requests
import json
import argparse
from datetime import datetime

def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError


def post_database(collection, params, jsondata):
    headers = {'content-type': 'application/json'}
    url = 'http://api_persistenciadados:5005/{}/'.format(collection)

    data = jsondata

    params = params
    response = requests.post(url, params=params, data=json.dumps(data), headers=headers)
    
    return response
   
def get_database(collection, params):
    url = 'http://api_persistenciadados:5005/{}/'.format(collection)
    params = params
    response = requests.get(url, params=params)

    return response


def delete_database(collection, params):
    url = 'http://api_persistenciadados:5005/{}/'.format(collection)
    params = params
    response = requests.delete(url, params=params)

    return response
    

def crud_main(method, company, collection, date='', jsondata=''):

    params = {}
    params['company'] = 'Cielo2' 

    if method == 'POST':
        if (date == ''):
            params['date'] = datetime.today().strftime('%Y%m%d')
        else:
            params['date'] = date

        print('DEBUG POST: {}'.format(params) )
        main_response = post_database(collection, params, jsondata)
    
    elif method == 'GET':
        if (date != ''):
            params['date'] = date

        print('DEBUG GET: {}'.format(params) )
        main_response = get_database(collection, params)

    elif method == 'DELETE':
        if (date != ''):
            params['date'] = date

        print('DEBUG DELETE: {}'.format(params) )
        main_response = delete_database(collection, params)
    
    print(main_response.status_code)
    print(main_response.text)


    #return main_response
