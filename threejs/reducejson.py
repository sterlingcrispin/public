# USAGE python reducejson.py INPUTFILE.json
# reads a threejs scene .json file and reduces the floating point decimal accuracy to 2
# and saves file as INPUTFILE_proccessed.json

import json
from sys import argv
import os
script, input_file = argv


json_data = open(input_file)
data = json.load(json_data)

for i in data['geometries']:
	
	if 'vertices' in i['data']:
		for idx, j in enumerate(i['data']['vertices']):
			 i['data']['vertices'][idx] = round(j,2)
	
	if 'normals' in i['data']:
		for idx, j in enumerate(i['data']['normals']):
			 i['data']['normals'][idx] = round(j,2)
	
	if 'uvs' in i['data']:
		for j in i['data']['uvs']:
			for idx, k in enumerate(j):
				j[idx] = round(k,2) 


newname = os.path.splitext(input_file)
newname = newname[0] + "_proccessed.json"

with open(newname, 'w') as outfile:
	json.dump(data, outfile, indent=0, sort_keys=True)

