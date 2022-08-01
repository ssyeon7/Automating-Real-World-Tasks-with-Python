import os
import requests

file_dir = "genericfilepath"
dict_keys = ['title', 'name', 'date', 'feedback']
file_list = os.listdir(file_dir)

for filename in file_list:
	fb_dict = {}
	file = os.path.join(file_dir, filename)
	with open(file) as fbfile:
		data = fbfile.read()
		lines = data.split('\n')
		for key, value in zip(dict_keys, lines):
			fb_dict[key] = value
	req = requests.post('http://<corpweb-external-IP>/feedback', json=fb_dict)
	print(req.status_code)

