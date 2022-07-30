from PIL import Image
import os

# Define the path for the image iteration and the final path to save the processed images
image_iter = os.path.join(os.path.expanduser('~'), "images", "")
final_path = os.path.join(os.path.expanduser('~'), "opt", "icons", "")

# Initialize the iteration of the images
for file in os.listdir(image_iter):
	# Set the absolute path of each image, so directory + file name
	input_path = os.path.join(image_iter, file)
	# Open the absolute path of each image
	try:
		with open(input_path, 'rb') as image:
			# Process each image
			im = Image.open(image)
			resized = im.resize((128,128))
			rotated = resized.rotate(270)
			formatted = rotated.convert("RGB")
			# Save the processed image to final_path, and join the file
			# as well as set the format to jpeg
			print(file[-5:])
			if file[-5:] == ".tiff" or file[-5:] == "jpeg":
				formatted.save(final_path + file[:-5] + ".jpeg", "JPEG")
			else:
				formatted.save(final_path + file[:-4] + ".jpeg", "JPEG")
	except OSError:
		pass

