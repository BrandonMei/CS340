import whoosh
import csv
from whoosh.index import open_dir
from whoosh.index import create_in
from whoosh.fields import *
import os, os.path

def index():
	colleges = ["ASU", "CAL", "OSU", "UFO"]
	if not os.path.exists("indexDir"):
		os.mkdir("indexDir")
	Header = ['firstName', 'lastName', 'Position', 'Height', 'Weight', 'Class', 'Hometown','Highschool','College']
	Header += ['CollegeFullName', 'mascot']
	Header += ["hit_AVG", "hit_GP", "hit_GS", "hit_AB", "hit_R", "hit_H", "hit_2B", "hit_3B", "hit_HR"]
	Header += ["hit_RBI", "hit_SLG%", "hit_BB", "hit_HBP", "hit_SO", "hit_GDP", "hit_OB%", "hit_SF"] 
	Header += ["hit_SH", "hit_SB", "hit_PO", "hit_A", "hit_E", "hit_FLD%"]
	Header += ["pitch_ERA", "pitch_W", "pitch_L", "pitch_APP", "pitch_GS", "pitch_CG", "pitch_SHO"]
	Header += ["pitch_SV", "pitch_IP", "pitch_H","pitch_R", "pitch_ER", "pitch_BB", "pitch_SO", "pitch_2B"]
	Header += ["pitch_3B", "pitch_HR", "pitch_BF", "pitch_BAVG", "pitch_WP", "pitch_HBP", "pitch_BK"]
	Header += ["pitch_SFA", "pitch_SHA"]
	schema = Schema()
	indexer = create_in("indexDir", schema)
	data = []
	for item in colleges:
		filename = item + ".csv"
		with open(filename, 'r') as csvfile:
			spamreader = csv.reader(csvfile, delimiter=',')
			for row in spamreader:
				if(row[0] != 'firstName'):
					temp = row + [item]
					data.append(temp)


	for item in data:
		print(item)
		print("---------------------")

	

	writer = indexer.writer()

	for item in Header:
		writer.add_field(item, TEXT(stored=True))

	for i in range(1,len(data)):
		writer.add_document(firstName=data[i][0], lastName=data[i][1], Position=data[i][2], Height=data[i][3], Weight=data[i][4], Class=data[i][5], Hometown=data[i][6], Highschool=data[i][7], College=data[i][8])

	writer.commit()
	print(str(len(data)) + " items writted")
	

	return 


def main():
	index()

main()

