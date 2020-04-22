#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Date: 20200316
User: Alan Viegas
Project:  Busca no site ReclameAqui.com.br por score-points e reclamations de uma Companhia

v101: Initial version

"""
import sys

# Para subir a API no Docker
sys.path.append('/app')

# Para subir localmente 
#sys.path.append('/home/alanviegas/Documentos/estudos/desafioSemantix/apps/API_consultaReclameAqui')

from flask import Flask, Response, jsonify, request, abort
from src.dao.reclamations import CompanyReclamations

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def home():
    return "API para consulta ao Reclame Aqui"

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
        