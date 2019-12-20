from bottle import Bottle, run, route, static_file, request, response, template
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId
import json
import pymongo
import requests
import time

app = Bottle(__name__)

client = MongoClient('mongodb://heroku_j47rhw75:2ctpo13v9ptj497mqf7q1o1aps@ds151909.mlab.com:51909/heroku_j47rhw75')
db = client.heroku_j47rhw75

@app.hook('after_request')
def enable_cors():
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
	response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'
	response.headers['Connection'] = 'keep-alive'

@app.route('/')
def root():
	return {'data': 'Server root'}

@app.route('/led/<uname>/<val>')
def led(uname, val):

	cur = db.iot_led.find({'uname': uname})
	data = json.loads(dumps(cur))

	if(len(data) == 0):
		cur = db.iot_led.insert({'uname': uname, 'val': val, 'time_stamp': time.time()})

		return {'response': 'New User Added', 'val': val}
	else:
		cur = db.iot_led.update({'uname': uname}, {'$set': {'val': val, 'time_stamp': time.time()}})

		return {'response': 'LED Toggled', 'val': val}

@app.route('/led/<uname>')
def led(uname):

	cur = db.iot_led.find({'uname': uname})
	data = json.loads(dumps(cur))
	
	return data[0]['val']

@app.route('/sensor/<uname>/<val>')
def sensor(uname, val):

	cur = db.iot_sensor.insert({'uname': uname, 'val': val, 'time_stamp': time.time()})

	return {'response': 'Sensor Value Added', 'val': val}
	
@app.route('/sensor/<uname>')
def sensor(uname):

	cur = db.iot_sensor.find({'uname': uname})
	data = json.loads(dumps(cur))
	
	return {'response': data}