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

{
  type: "MultiPoint",
  coordinates: [
     [ 13.0445588, 77.6201398 ],
     [ 13.0448949, 77.6197818 ],
  ]
}
 
run(reloader=True, debug=True, host='mighty-brook-54547.herokuapp.com', port=8080)
