#!python
# Copyright 2021 Alexander Sosna <alexander@sosna.de>
#
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.

import requests
import yaml
import os
import re
import time
import json

config_file="snakeoil-mill.yaml"

# Run in client mode
def client(config):
	results = {
			'username':config['username'],
			'password':config['password'],
		}

	# Execute all configured commands and sore the results
	for item in config['commands']:
		name, cmd = item.popitem()
		stream = os.popen(cmd)
		output = stream.read()

		# strip newlines and save results
		results[name] = re.sub(r"[\n]*", "", output)

	print(results)

	# Send the results to our backend server
	print(results)
	r = requests.post(config['api'], data=results)
	print("REQUEST:")
	print(r.text)
	return 0

def main():
	# Open and load the configuration
	with open(config_file, 'r') as config_raw:
		try:
			config = yaml.load(config_raw, Loader=yaml.SafeLoader)
			print(config)
		except yaml.YAMLError as exc:
			print(exc)

	if config['mode'] == 'client':
		while (1):
			client(config)
			print("sleep now")
			time.sleep(int(config['loop_time_s']))
			print("sleep done")
	else:
		print("error: config not for client")
		exit(1)

if __name__ == "__main__":
	main()