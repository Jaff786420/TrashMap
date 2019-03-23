from bottle import Bottle, run, route, static_file, request, response, template, get, post
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId
import json
import pymongo
import requests
import time
import random

app = Bottle(__name__)

client = MongoClient('mongodb://heroku_j47rhw75:2ctpo13v9ptj497mqf7q1o1aps@ds151909.mlab.com:51909/heroku_j47rhw75')
db = client.heroku_j47rhw75

col=db['dustbin']

@app.hook('after_request')
def enable_cors():
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
	response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
	response.headers['Connection'] = 'keep-alive'

@get('/dustbin')
def getAll():
	for x in col.find():
  		print(x) 

"""@get('/animal/<name>')
def getOne(name):
	the_animal = [animal for animal in animals if animal['name'] == name]
	return {'animal' : the_animal[0]}"""

@post('/dustbin')
def addOne():
	new_dustbin = {'id': random.randint(1,1000), 'area' : request.json.get('area'), 'size' : request.json.get('size')}
	"""dustbins.append(new_dustbin)"""
	x=col.insert_one(new_dustbin)
	

"""@delete('/dustbin/<id>')
def removeOne(name):
	the_dustbin = [dustbin for dustbin in dustbins if dustbin['id'] == id]
	dustbins.remove(the_dustbin[0])
	return {'dustbins' : dustbins}


	myquery = { "id": "Mountain 21" }

	mycol.delete_one(myquery) 
"""
run(reloader=True, debug=True, host='127.0.0.1', port=8080)
