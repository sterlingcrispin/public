import json
from sys import argv
import os
script, input_file = argv


json_data = open(input_file)
data = json.load(json_data)

for i in data['geometries']:
	
	if 'vertices' in i['data']:
		for idx, j in enumerate(i['data']['vertices']):
			x = i['data']['vertices'][idx]
			if isinstance(x, (int, long, float, complex)):
				i['data']['vertices'][idx] = round(j,2)
	
	if 'normals' in i['data']:
		for idx, j in enumerate(i['data']['normals']):
			x = i['data']['vertices'][idx]
			if isinstance(x, (int, long, float, complex)):
				i['data']['normals'][idx] = round(j,2)
	
	if 'uvs' in i['data']:
		for j in i['data']['uvs']:
			for idx, k in enumerate(j):
				x = j[idx]
				if isinstance(x, (int, long, float, complex)):
					j[idx] = round(k,2) 


newname = os.path.splitext(input_file)
newname = newname[0] + "_proccessed.json"

with open(newname, 'w') as outfile:
	json.dump(data, outfile, indent=0, sort_keys=True)

