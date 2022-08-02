#!/usr/bin/env python3

import os
import requests


def fruit_data(url, desc_dir):
	dict_keys = ["name", "weight", "description", "image_name"]
	file_list = os.listdir(desc_dir)
	fruit_dict = {}
	for filename in file_list:
		fruit_dict.clear()
		keycount = 0
		with open(desc_dir + filename) as fruitfile:
			for line in fruitfile:
				lines = line.strip()
				fruit_dict[dict_keys[keycount]] = lines
				keycount += 1
		wvalue = fruit_dict.get('weight').strip('lbs')
		fruit_dict["weight"] = int(wvalue)
		fruit_dict["image_name"] = filename.replace(".txt", ".jpeg")
		if url != "":
			req = requests.post(url, json=fruit_dict)
			print(req.request.url)
			print(req.status_code)
	return 0


if __name__ == '__main__':
	url = 'http://localhost/fruits/'
	user = os.getenv('USER')
	desc_dir = '/home/{}/supplier-data/descriptions/'.format(user)
	fruit_data(url, desc_dir)
