import json
from sys import argv
import os
script, input_file = argv


json_data = open(input_file)
data = json.load(json_data)

for i in data['geometries']:
	
	if 'array' in i['data']['attributes']['position']:
		for idx, j in enumerate(i['data']['attributes']['position']['array']):
			x = i['data']['attributes']['position']['array'][idx]
			if isinstance(x, (int, long, float, complex)):
				i['data']['attributes']['position']['array'][idx] = round(j,2)
	
	if 'normal' in i['data']['attributes']:
		if 'array' in i['data']['attributes']['normal']:
			for idx, j in enumerate(i['data']['attributes']['normal']['array']):
				x = i['data']['attributes']['normal']['array'][idx]
				if isinstance(x, (int, long, float, complex)):
					i['data']['attributes']['normal']['array'][idx] = round(j,2)
		
	if 'uv' in i['data']['attributes']:
		if 'array' in i['data']['attributes']['uv']:
			for idx, j in enumerate(i['data']['attributes']['uv']['array']):
				i['data']['attributes']['uv']['array'][idx] = round(j,2)
	

newname = os.path.splitext(input_file)
newname = newname[0] + "_proccessed.json"

with open(newname, 'w') as outfile:
	json.dump(data, outfile, indent=0)

