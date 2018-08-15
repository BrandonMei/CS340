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
	Header += ["hit_RBI", "hit_SLG", "hit_BB", "hit_HBP", "hit_SO", "hit_GDP", "hit_OB", "hit_SF"] 
	Header += ["hit_SH", "hit_SB", "hit_PO", "hit_A", "hit_E", "hit_FLD"]
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




	

	writer = indexer.writer()

	for item in Header:
		writer.add_field(item, TEXT(stored=True))

	for i in range(1,len(data)):
		writer.add_document(firstName=data[i][0], lastName=data[i][1], Position=data[i][2], Height=data[i][3], Weight=data[i][4], Class=data[i][5], Hometown=data[i][6], Highschool=data[i][7], College=data[i][8],CollegeFullName = data[i][9],mascot=data[i][10],hit_AVG = data[i][11], hit_GP=data[i][12], hit_GS=data[i][13], hit_AB=data[i][14],hit_R = data[i][15], hit_H=data[i][16], hit_2B=data[i][17], hit_3B=data[i][18],hit_HR=data[i][19], hit_RBI=data[i][20], hit_SLG=data[i][21], hit_BB=data[i][22],hit_HBP=data[i][23], hit_SO=data[i][24], hit_GDP=data[i][25], hit_OB=data[i][26],hit_SF=data[i][27], hit_SH=data[i][28],hit_SB=data[i][29],hit_PO=data[i][30],hit_A=data[i][31], hit_E=data[i][32], hit_FLD=data[i][33],pitch_ERA = data[i][34],pitch_W=data[i][35],pitch_L=data[i][36],pitch_APP=data[i][37],pitch_GS=data[i][38],pitch_CG=data[i][39],pitch_SHO=data[i][40],pitch_SV=data[i][41],pitch_IP=data[i][42],pitch_H=data[i][43],pitch_R=data[i][44],pitch_ER=data[i][45],pitch_BB=data[i][46],pitch_SO=data[i][47],pitch_2B=data[i][48],pitch_3B=data[i][49],pitch_HR=data[i][50],pitch_BF=data[i][51],pitch_BAVG=data[i][52],pitch_WP=data[i][53],pitch_HBP=data[i][54],pitch_BK=data[i][55],pitch_SFA=data[i][56],pitch_SHA=data[i][57])
		#writer.add_document(CollegeFullName = data[i][9],mascot=data[i][10])
		#writer.add_document(hit_AVG = data[i][11], hit_GP=data[i][12], hit_GS=data[i][13], hit_AB=data[i][14])
		#writer.add_document(hit_R = data[i][15], hit_H=data[i][16], hit_2B=data[i][17], hit_3B=data[i][18])
		#writer.add_document(hit_HR=data[i][19], hit_RBI=data[i][20], hit_SLG=data[i][21], hit_BB=data[i][22])
		#writer.add_document(hit_HBP=data[i][23], hit_SO=data[i][24], hit_GDP=data[i][25], hit_OB=data[i][26])
		#writer.add_document(hit_SF=data[i][27], hit_SH=data[i][28],hit_SB=data[i][29],hit_PO=data[i][30])
		#writer.add_document(hit_A=data[i][31], hit_E=data[i][32], hit_FLD=data[i][33])
		#writer.add_document(pitch_ERA = data[i][34],pitch_W=data[i][35],pitch_L=data[i][36],pitch_APP=data[i][37])
		#writer.add_document(pitch_GS=data[i][38],pitch_CG=data[i][39],pitch_SHO=data[i][40])
		#writer.add_document(pitch_SV=data[i][41],pitch_IP=data[i][42],pitch_H=data[i][43],pitch_R=data[i][44])
		#writer.add_document(pitch_ER=data[i][45],pitch_BB=data[i][46],pitch_SO=data[i][47],pitch_2B=data[i][48])
		#writer.add_document(pitch_3B=data[i][49],pitch_HR=data[i][50],pitch_BF=data[i][51],pitch_BAVG=data[i][52])
		#writer.add_document(pitch_WP=data[i][53],pitch_HBP=data[i][54],pitch_BK=data[i][55],pitch_SFA=data[i][56],pitch_SHA=data[i][57])
	writer.commit()
	print(str(len(data)) + " items writted")
	

	return 


def main():
	index()

main()

