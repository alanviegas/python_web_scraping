#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Date: 20200413
User: Alan Viegas
Project: API para fazer um Rest API de CRUD básico para persistir os dados do ReclameAqui
v101: Initial version

## Tests 
    curl -X POST "http://localhost:5005/scores?company=Cielo&date=20200421"
    curl -X GET "http://localhost:5005/scores?company=Cielo"
    curl -X DELETE "http://localhost:5005/scores?company=Cielo&date=20200421"
    curl -X DELETE "http://localhost:5005/scores?company=Cielo"

Ref:
    https://pynative.com/python-json-validation/

"""

import sys

# Para subir a API no Docker
sys.path.append('/app')

# Para subir localmente 
#sys.path.append('/home/alanviegas/Documentos/estudos/desafioSemantix/apps/API_persistenciaDados')

import json
from flask import Flask, Response, jsonify, request, abort
from datetime import datetime
from src.dao.model import ReclameAquiScore, ReclameAquiReclamation
from utils.utils import validateJSON

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def home():
    return "API para fazer um Rest API de CRUD básico para persistir os dados do ReclameAqui"


@app.route('/scores/', methods=['POST'])
def post_scores():
    company = request.args['company']
    date = request.args['date']
    
    json_raw = request.get_json()

    isValid = validateJSON(json_raw, 'scores')
    if not isValid:
        return jsonify({'Formato Invalido', 400})

    json_id = {'_id' : date + company.upper(), 'company' : company, 'date' : date}
    json_final = {**json_id, **json_raw}
  
    score = ReclameAquiScore(**json_final)
    score.save()
    id = score._id

    response = app.response_class(
                    response=json.dumps({'id': str(id)}),
                    status=200,
                    mimetype='application/json'
    )
    return response

@app.route('/reclamations/', methods=['POST'])
def post_reclamations():
    company = request.args['company']
    date = request.args['date']
    
    json_raw = request.get_json()

    isValid = validateJSON(json_raw, 'reclamations')
    if not isValid:
        return jsonify({'Formato Invalido', 400})

    result = {}
    for key in json_raw:
        json_id = {'_id' : date + company.upper() + key, 'company' : company, 'date' : date}
        json_final = {**json_id, **json_raw['{}'.format(key)]}
        reclamations = ReclameAquiReclamation(**json_final)
        reclamations.save()
        
        result[str(reclamations._id)] = str('ok')
        
    response = app.response_class(
                   response=json.dumps(result),
                   status=200,
                   mimetype='application/json'
    )
    return response


@app.route('/scores/', methods=['GET'])
def get_scores():
    company = request.args['company']

    scores = ReclameAquiScore({"company": company})
    scores = scores.query
    
    result = {}
    for score in scores:
        id = score['_id']
        company = score['company']
        date = score['date']
        answered = score['answered']
        reclamations = score['reclamations']
        response_time = score['response_time']
        unanswered = score['unanswered']
 
        result[str(id)] = {'company' : company, 
                           'date' : date , 
                           'answered' : answered, 
                           'reclamations' : reclamations, 
                           'response_time' : response_time,
                           'unanswered' : unanswered}
  
    response = app.response_class(
                response=json.dumps(result),
                status=200,
                mimetype='application/json',
    )
    return response


@app.route('/reclamations/', methods=['GET'])
def get_reclamations():
    company = request.args['company']
    if 'date' in request.args:
        date = request.args['date']
    else:
        date = None
    
    if date is None:
        reclamations = ReclameAquiReclamation({"company": company})
    else:
        reclamations = ReclameAquiReclamation({"company": company, "date": date})

    reclamations = reclamations.query
        
    result = {}
    for reclamation in reclamations:
        id = reclamation['_id']
        company = reclamation['company']
        date = reclamation['date']
        description = reclamation['description']
        locale_date = reclamation['locale_date']
        title = reclamation['title']
        
        result[str(id)] = {'company' : company, 
                            'date' : date , 
                            'description' : description, 
                            'locale_date' : locale_date, 
                            'title' : title}
    
    response = app.response_class(
                response=json.dumps(result, ensure_ascii=False),
                status=200,
                mimetype='application/json'
    )
    return response


@app.route('/scores/', methods=['DELETE'])
def delete_scores():
    company = request.args['company']
    if 'date' in request.args:
        date = request.args['date']
    else:
        date = None
    
    if date is None:
        scores = ReclameAquiScore({"company": company})
        scores = scores.remove_all
        return jsonify('Deleted')
        
    json_id = {'_id' : date + company.upper()}
    score = ReclameAquiScore(json_id)
    score.remove()
    return jsonify('Deleted')


@app.route('/reclamations/', methods=['DELETE'])
def delete_reclamations():
    company = request.args['company']
    if 'date' in request.args:
        date = request.args['date']
    else:
        date = None
    
    if date is None:
        reclamations = ReclameAquiReclamation({"company": company})
        reclamations = reclamations.remove_all
        return jsonify('Deleted')
    else:
        reclamations = ReclameAquiReclamation({"company": company, "date": date})
        reclamations = reclamations.remove_all
        return jsonify('Deleted')


if __name__ == '__main__':
    try:
        app.run(debug=True, host='0.0.0.0', port=5005)
    except:
        abort(400)
        