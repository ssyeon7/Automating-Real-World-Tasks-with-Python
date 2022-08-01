#! /usr/bin/env python3

import os
import requests

file_dir = "/data/feedback/"
dict_keys = ["title", "name", "date", "feedback"]
file_list = os.listdir(file_dir)

for filename in file_list:
	keycount = 0
	fb_dict = {}
	with open(file_dir + filename) as fbfile:
		for line in fbfile:
			lines = line.strip()
			fb_dict[dict_keys[keycount]] = lines
			keycount += 1
	print(fb_dict)
	req = requests.post("http://<corpweb-external-IP>/feedback", json=fb_dict)

print(req.request.body)
print(req.status_code)
