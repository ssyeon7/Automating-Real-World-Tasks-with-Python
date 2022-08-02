#!/usr/bin/env python3

import requests
import os

url = "http://localhost/upload/"
image_iter = os.path.join(os.path.expanduser('~'), "supplier-data", "images", "")

for file in os.listdir(image_iter):
	if not file.startswith('.') and 'jpeg' in file:
		input_path = os.path.join(image_iter, file)
		with open(input_path, 'rb') as image:
			r = requests.post(url, files={'file': image})
