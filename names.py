#! /usr/bin/python

import os.path

print "Jmena lektoru kurzu:"

lecturers = [
	"Honza",
	"Vlasta",
	"Bizi",
	"Mira"
	]

for name in lecturers:
	print name

print "\nJmena ucastniku kurzu:"

students = [
	"Eva",
	"Pavel",
	"Frantisek"
	]

for name in students:
	print name
	filename = name.lower() + ".txt"
	if os.path.isfile(filename):
		with open(filename, 'r') as content_file:
		    content = content_file.read()
		print content
