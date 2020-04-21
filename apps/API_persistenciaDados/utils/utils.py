#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
#sys.path.append('/app')

from pathlib import Path
import json
import jsonschema


def get_project_root():
    """Returns project root folder."""
    return Path(__file__).parent.parent

def get_url():
    return 'https://www.reclameaqui.com.br'
    #return '107.154.102.99'

def validateJSON(jsonData, schema):
    
    scoresSchema = {
        "type": "object",
        "maxProperties": 4,
        "properties": {
                "answered": {"type": "string"}, 
                "reclamations": {"type": "string"}, 
                "response_time": {"type": "string"}, 
                "unanswered": {"type": "string"}
                 },
        "additionalProperties": False
        }
              
    reclamationsSchema = {
        "type": "object",
        "maxProperties": 10,
        "properties": { "number": {
                            "type": "object",
                            "maxProperties": 3,
                            "properties": { 
                                "description": {"type": "string"}, 
                                "locale_date": {"type": "string"}, 
                                "title": {"type": "string"} 
                            },
                            "additionalProperties": False
                          }
                       }
        }

    json_valid = True
    
    try:
        json.dumps(jsonData)
    except ValueError as err:
        json_valid = False
   
    if (schema == 'scores'):
        try:
            jsonschema.validate(instance=jsonData, schema=scoresSchema)
        except jsonschema.exceptions.ValidationError as err:
            json_valid = False
    
    if (schema == 'reclamations'):
        try:
            jsonschema.validate(instance=jsonData, schema=reclamationsSchema)
        except jsonschema.exceptions.ValidationError as err:
            json_valid = False
  
    return json_valid