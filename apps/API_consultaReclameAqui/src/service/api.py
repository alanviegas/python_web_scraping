#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Date: 20200316
User: Alan Viegas
Project: Search on site ReclameAqui.com for score-points and reclamations of the Company

# Tests 
# curl -X GET "http://localhost:5000/scores?company=Cielo"
# curl -X GET "http://localhost:5000/reclamations?company=Cielo"

R0: Initial version
"""

import sys
sys.path.append('/app')
#sys.path.append('/home/alanviegas/Documentos/estudos/desafioSemantix/apps/API_consultaReclameAqui')

from flask import Flask, Response, jsonify, request, abort
from src.dao.reclamations import CompanyReclamations

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False



@app.route('/')
def home():
    return "API para consulta ao Reclame Aqui"

'''
## curl -X GET "http://localhost:5000/test1?tk=50"
@app.route('/test1', methods=['GET'])
def foo8():
    cr = CR()
    try:
       var2 = int(request.args['tk'])
    except:
        abort(400)
  
    return jsonify(status='Codigo realizado {}'.format(var2))
'''

@app.route('/scores', methods=['GET'])
def get_scores():
    company = request.args['company']
    cr = CompanyReclamations()
    cr.search_company(company)
    scores = cr.get_scores
    cr.close()

    return jsonify(scores)


@app.route('/reclamations', methods=['GET'])
def get_reclamations():
    company = request.args['company']
    cr = CompanyReclamations()
    cr.search_company(company)
    reclamations = cr.get_reclamations
    cr.close()

    return jsonify(reclamations)


if __name__ == '__main__':
    try:
        app.run(debug=True, host='0.0.0.0', port=5000)
    except:
        abort(400)
        