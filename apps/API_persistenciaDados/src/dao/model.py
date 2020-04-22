#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Date: 20200413
User: Alan Viegas
Project: criação, consulta, atualização e remoção de dados no MongoDB
v101: Initial version
 
## Dados do banco 
    #Para entrar na docker
    docker exec -it mongodb bash

    #para comitar as alteracoes da docker
    docker commit <container-id> mmongo:3.6.3

conexao mongodb://127.0.0.1:27017
 
Criação do banco
    mongo --port 27017 -u root -p root --authenticationDatabase "admin"
    use reclameaqui-db

    db.createCollection("scores")
    db.createCollection("reclamations")

    db.createUser( {
        user:"appuser",
        pwd: "senha123",   // Instead of specifying the password in cleartext
        roles:[ "readWrite" ]
    } )

## Teste conexao
    mongo -u appuser -p senha123 --authenticationDatabase reclameaqui-db



Refs: 
https://www.bogotobogo.com/python/MongoDB_PyMongo/python_MongoDB_pyMongo_tutorial_installing.php
https://gist.github.com/fatiherikli/4350345

"""

from pymongo import MongoClient
from datetime import datetime

# -----------------------------------------
# Um modelo simples para documentos mongodb
# -----------------------------------------
class Model(dict):
    __getattr__ = dict.get
    __delattr__ = dict.__delitem__
    __setattr__ = dict.__setitem__
 
    def save(self):
        self.collection.update( { "_id": self._id }, 
                                self,
                                upsert = True )

    def reload(self):
        if self._id:
            self.update(self.collection.find_one({"_id": self._id}))

    def remove(self):
        if self._id:
            self.collection.remove({"_id": self._id})
            self.clear()

    @property
    def query(self):
        return list(self.collection.find(self))
    
    @property
    def remove_all(self):
        self.collection.delete_many(self)
        self.clear()

# ------------------------------
# Documento Scores com as configuracoes de conexao ao mongoDB
# ------------------------------

class ReclameAquiScore(Model):
    __uri = "mongodb://appuser:senha123@mongodb:27017/reclameaqui-db"
    __client = MongoClient(__uri)
    __db = __client['reclameaqui-db']

    collection = __db.get_collection('scores')
   

# ------------------------------
# Documento Reclamations com as configuracoes de conexao ao mongoDB
# ------------------------------
class ReclameAquiReclamation(Model):
    __uri = "mongodb://appuser:senha123@mongodb:27017/reclameaqui-db"
    __client = MongoClient(__uri)
    __db = __client['reclameaqui-db']
    collection = __db.get_collection('reclamations')
