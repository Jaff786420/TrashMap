
from bottle import Bottle, run, route, static_file, request, response, template, redirect
from pymongo import MongoClient
from bson.json_util import dumps
from bson.objectid import ObjectId
from string import Template
import json
import pymongo
import requests
import datetime
import time
import math
import hashlib as hl
import os
import smtplib
import boto3
import uuid
app = Bottle(__name__)


@app.route('/sign_s3')
def sign_s3():

	print(request.GET.get('file_name'))

	S3_BUCKET = 'trashbin2'

	file_name = request.GET.get('file_name')
	file_type = request.GET.get('file_type')

	s3 = boto3.client('s3')

	presigned_post = s3.generate_presigned_post(
		Bucket = S3_BUCKET,
		Key = file_name,
		Fields = {"acl": "public-read", "Content-Type": file_type},
		Conditions = [
		  {"acl": "public-read"},
		  {"Content-Type": file_type}
		],
		ExpiresIn = 3600
	)

	return json.dumps({
	'data': presigned_post,
	'url': 'https://%s.s3.amazonaws.com/%s' % (S3_BUCKET, file_name)
	})
