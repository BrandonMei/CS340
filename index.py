import whoosh
import csv
from whoosh.index import open_dir
from whoosh.index import create_in
from whoosh.fields import *
import os, os.path

def index():
	if not os.path.exists("indexDir"):
		os.mkdir("indexDir")
	Header = ['firstName', 'lastName', 'Position', 'Height', 'Weight', 'Class', 'Hometown','Highschool']
	schema = Schema()
	indexer = create_in("indexDir", schema)

	with open('OSU.csv', 'r') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',')
		data = []
		for row in spamreader:
			data.append(row)

	writer = indexer.writer()

	for item in Header:
		writer.add_field(item, TEXT(stored=True))

	for i in range(1,len(data)):
		writer.add_document(firstName=data[i][0], lastName=data[i][1], Position=data[i][2], Height=data[i][3], Weight=data[i][4], Class=data[i][5], Hometown=data[i][6], Highschool=data[i][7])

	writer.commit()

	return indexer

def main():
	index()

main()

