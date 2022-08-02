#!/usr/bin/env python3

from PIL import Image
import os

image_iter = os.path.join(os.path.expanduser('~'), "supplier-data", "images", "")

for file in os.listdir(image_iter):
	input_path = os.path.join(image_iter, file)
	try:
		with open(input_path, 'rb') as image:
			im = Image.open(image)
			formatted = im.convert("RGB")
			resized = formatted.resize((600, 400))
			resized.save(input_path[:-5] + ".jpeg", "JPEG")
	except OSError:
		pass
