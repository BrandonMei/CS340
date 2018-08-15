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
		result=[[],[],[],[],[],[],[],[],[],[]]
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
			result[9].append(line['CollegeFullName'])
		return result

def search_stats(indexer, searchTerm, searchColumns):
	with indexer.searcher() as searcher:
		words = searchColumns
		query = MultifieldParser(words, schema=indexer.schema).parse(searchTerm)
		results = searcher.search(query,limit=None)
		print(results)
		result=[]
		Header = ["firstName", "lastName", "Position", "Height", "Weight", "Class", "Hometown", "CollegeFullName"]
		Header += ["hit_AVG", "hit_GP", "hit_GS", "hit_AB", "hit_R", "hit_H", "hit_2B", "hit_3B", "hit_HR"]
		Header += ["hit_RBI", "hit_SLG", "hit_BB", "hit_HBP", "hit_SO", "hit_GDP", "hit_OB", "hit_SF"] 
		Header += ["hit_SH", "hit_SB", "hit_PO", "hit_A", "hit_E", "hit_FLD"]
		Header += ["pitch_ERA", "pitch_W", "pitch_L", "pitch_APP", "pitch_GS", "pitch_CG", "pitch_SHO"]
		Header += ["pitch_SV", "pitch_IP", "pitch_H","pitch_R", "pitch_ER", "pitch_BB", "pitch_SO", "pitch_2B"]
		Header += ["pitch_3B", "pitch_HR", "pitch_BF", "pitch_BAVG", "pitch_WP", "pitch_HBP", "pitch_BK"]
		Header += ["pitch_SFA", "pitch_SHA"]

		for line in results:
			for item in Header:
				result.append([])
				result[len(result)-1].append(line[item])
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
	#print(query)
	Header = ['firstName', 'lastName', 'Position', 'Height', 'Weight', 'Class', 'Hometown','Highschool','College']
	dx = open_dir("indexDir")
	#Header = ['Class']
	result = search(dx, query, Header)
	print(result)
	img = []
	for i in range(len(result[8])):
		temp = str(result[8][i]) + "/image/" + str(result[0][i]) + "_" + str(result[1][i]) +".jpg"
		img.append(temp)
	return render_template('index.html', query=query, results=zip(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[9], img), scroll="result")

@app.route('/Modal/', methods=['GET', 'POST'])
def Modal():
	if request.method == 'POST':
		data = request.form
	else:
		data = request.args
	query = data.get('query')
	img = data.get('img')
	first = data.get('firstName')
	last = data.get('lastName')
	coll = data.get('College')
	keyword = first +' ' + last + ' ' + coll
	Header = ['firstName', 'lastName', 'Position', 'Height', 'Weight', 'Class', 'Hometown','Highschool','College']
	Header += ['CollegeFullName', 'mascot']
	Header += ["hit_AVG", "hit_GP", "hit_GS", "hit_AB", "hit_R", "hit_H", "hit_2B", "hit_3B", "hit_HR"]
	Header += ["hit_RBI", "hit_SLG", "hit_BB", "hit_HBP", "hit_SO", "hit_GDP", "hit_OB", "hit_SF"] 
	Header += ["hit_SH", "hit_SB", "hit_PO", "hit_A", "hit_E", "hit_FLD"]
	Header += ["pitch_ERA", "pitch_W", "pitch_L", "pitch_APP", "pitch_GS", "pitch_CG", "pitch_SHO"]
	Header += ["pitch_SV", "pitch_IP", "pitch_H","pitch_R", "pitch_ER", "pitch_BB", "pitch_SO", "pitch_2B"]
	Header += ["pitch_3B", "pitch_HR", "pitch_BF", "pitch_BAVG", "pitch_WP", "pitch_HBP", "pitch_BK"]
	Header += ["pitch_SFA", "pitch_SHA"]
	dx = open_dir("indexDir")
	result = search_stats(dx, keyword, Header)
	return render_template('detail.html', query=query, img = img,stats=zip(result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7]), scroll="myModal")




if __name__ == '__main__':
	app.run(debug=True)
