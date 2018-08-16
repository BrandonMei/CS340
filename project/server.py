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
		result=[]
		Header = ['firstName', 'lastName', 'Position', 'Height', 'Weight', 'Class', 'Hometown','Highschool','College']
		Header += ['CollegeFullName', 'mascot']
		Header += ["hit_AVG", "hit_GP", "hit_GS", "hit_AB", "hit_R", "hit_H", "hit_2B", "hit_3B", "hit_HR"]
		Header += ["hit_RBI", "hit_SLG", "hit_BB", "hit_HBP", "hit_SO", "hit_GDP", "hit_OB", "hit_SF"] 
		Header += ["hit_SH", "hit_SB", "hit_PO", "hit_A", "hit_E", "hit_FLD"]
		Header += ["pitch_ERA", "pitch_W", "pitch_L", "pitch_APP", "pitch_GS", "pitch_CG", "pitch_SHO"]
		Header += ["pitch_SV", "pitch_IP", "pitch_H","pitch_R", "pitch_ER", "pitch_BB", "pitch_SO", "pitch_2B"]
		Header += ["pitch_3B", "pitch_HR", "pitch_BF", "pitch_BAVG", "pitch_WP", "pitch_HBP", "pitch_BK"]
		Header += ["pitch_SFA", "pitch_SHA"]
		counter = 1
		for line in results:
			temp={}
			for item in Header:
				temp[item] = line[item]
				temp["counter"] = counter
			result.append(temp)
			counter+=1
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
	#Header = ['firstName', 'lastName', 'Position', 'Height', 'Weight', 'Class', 'Hometown','Highschool','College']
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
	#Header = ['Class']
	result = search(dx, query, Header)
	print("-----------------")
	print(result)
	img = []
	for item in result:
		#print(item)
		img = item['College'] + "/image/" + item["firstName"] + "_" + item["lastName"] + ".jpg"
		item["img"] = img
	leng = len(result)
	return render_template('index.html', query=query, results=result,stats=result,scroll="result",leng=leng)

if __name__ == '__main__':
	app.run(debug=True)
