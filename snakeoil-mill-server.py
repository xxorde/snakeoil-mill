#!python
# Alexander Sosna <alexander@sosna.de>
import requests
import yaml
import os
import re
import time
from flask import Flask
from flask import request

app = Flask(__name__)

config_file="snakeoil-mill-server.yaml"

# Open and load the configuration
with open(config_file, 'r') as config_raw:
	try:
		config = yaml.load(config_raw, Loader=yaml.SafeLoader)
		print(config)
	except yaml.YAMLError as exc:
		print(exc)

if config['mode'] != 'server':
	print("error: config not for server")
	exit(1)


@app.route('/submit', methods=['POST'])
def submit():
	print("REQUEST")
	print(request)
	ret = "nice"
	if valid_login(request.form['username'], request.form['password']):
		print("DEBUG:")
		ret=str(request.form)
		print(ret)
		#print(request.args.get('results', ''))
	else:
		ret = 'Invalid username/password'
	return ret

@app.route('/health')
def health():
	return "{'health': 'ok'}"

# Check if the user is allowed to submit data
def valid_login(username, password):
	return True