#!/usr/bin/env python3

import datetime
import os

from reports import fruit_report
from emails import generate_email, send_email


def pdf_body(input, desc_dir):
	"""Generating a summary with two lists, which gives the output name and weight"""
	names = []
	weights = []
	for item in os.listdir(desc_dir):
		filename = os.path.join(desc_dir, item)
		with open(filename) as f:
			line = f.readlines()
			weight = line[1].strip('\n')
			name = line[0].strip('\n')
			names.append('name: ' + name)
			weights.append('weight: ' + weight)
	new_obj = ""
	for i in range(len(names)):
		if names[i] and input == 'pdf':
			new_obj += names[i] + '<br/>' + weights[i] + '<br/>' + '<br/>'
	return new_obj


if __name__ == "__main__":
	user = os.getenv('USER')
	desc_dir = '/home/{}/supplier-data/descriptions/'.format(user)
	current_date = datetime.date.today().strftime("%B %d, %Y")
	title = 'Processed Update on ' + str(current_date)
	fruit_report('/tmp/processed.pdf', title, pdf_body('pdf', desc_dir))
	email_subject = 'Upload Completed - Online Fruit Store'
	email_body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
	email = generate_email("automation@example.com", "<username>@example.com".format(user), email_subject, email_body, "/tmp/processed.pdf")
	send_email(email)
