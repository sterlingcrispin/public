# USAGE python reducejson.py INPUTFILE.json
# reads a threejs scene .json file of BUFFER GEOMETRY
# and reduces the floating point decimal accuracy to 2
# and saves file as INPUTFILE_proccessed.json

import json
from sys import argv
import os
script, input_file = argv


json_data = open(input_file)
data = json.load(json_data)

for i in data['geometries']:
	
	if 'array' in i['data']['attributes']['position']:
		for idx, j in enumerate(i['data']['attributes']['position']['array']):
			i['data']['attributes']['position']['array'][idx] = round(j,2)
	
	if 'array' in i['data']['attributes']['normal']:
		for idx, j in enumerate(i['data']['attributes']['normal']['array']):
			i['data']['attributes']['normal']['array'][idx] = round(j,2)
	

	if 'array' in i['data']['attributes']['uv']:
		for idx, j in enumerate(i['data']['attributes']['uv']['array']):
			i['data']['attributes']['uv']['array'][idx] = round(j,2)
	

newname = os.path.splitext(input_file)
newname = newname[0] + "_proccessed.json"

with open(newname, 'w') as outfile:
	json.dump(data, outfile, indent=0)

