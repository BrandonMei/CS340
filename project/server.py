from flask import Flask, render_template, url_for, request
import sys
import whoosh
import os, os.path
from whoosh.index import open_dir
from whoosh.index import create_in
from whoosh.fields import *
from whoosh.qparser import QueryParser
from whoosh.qparser import MultifieldParser

def search(indexer, searchTerm, searchColumns):
	with indexer.searcher() as searcher:
		words = searchColumns
		query = MultifieldParser(words, schema=indexer.schema).parse(searchTerm)
		results = searcher.search(query,limit=None)
		print(results)
		result=[[],[],[],[],[],[],[],[],[]]
		for line in results:
			result[0].append(line['firstName'])
			result[1].append(line['lastName'])
			result[2].append(line['Position'])
			result[3].append(line['Height'])
			result[4].append(line['Weight'])
			result[5].append(line['Class'])
			result[6].append(line['Hometown'])
			result[7].append(line['Highschool'])
			result[8].append(line['College'])
		return result



app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')

@app.route('/result/', methods=['GET', 'POST'])
def result():
	if request.method == 'POST':
		data = request.form
	else:
		data = request.args
	query = data.get('keywords')
	Header = ['firstName', 'lastName', 'Position', 'Height', 'Weight', 'Class', 'Hometown','Highschool','College']
	dx = open_dir("indexDir")
	#Header = ['Class']
	result = search(dx, query, Header)
	print(result)
	img = []
	for i in range(len(result[8])):
		temp = str(result[8][i]) + "/image/" + str(result[0][i]) + "_" + str(result[1][i]) +".jpg"
		img.append(temp)
	return render_template('result.html', query=query, results=zip(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], img))




if __name__ == '__main__':
	app.run(debug=True)