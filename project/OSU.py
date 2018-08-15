import requests
from bs4 import BeautifulSoup
import string
from selenium import webdriver
import time




page = requests.get('https://osubeavers.com/roster.aspx?path=baseball',headers={'User-Agent': 'Custom'})
#page = requests.get("https://google.com")
#print(page.status_code)
html = page.text

soup = BeautifulSoup(html, "html.parser")
name = soup.find_all("td","sidearm-table-player-name")

flag = 0
driver = webdriver.Chrome()
driver.maximize_window()

for item in name:
	newurl = "https://osubeavers.com" + item.a.get("href")
	driver.get(newurl)
	time.sleep(5)
	element = driver.find_element_by_id("ui-id-3")
	element.click()
	time.sleep(2)
	

	#personalPage = requests.get(newurl,headers={'User-Agent': 'Custom'})
	#temp = personalPage.text

	newsoup = BeautifulSoup(driver.page_source.encode('utf-8').strip(), "html.parser")
	names = newsoup.find("span", "sidearm-roster-player-name")
	firstName = names.find_all("span")[0].get_text()
	lastName = names.find_all("span")[1].get_text()
	'''
	image = "https://osubeavers.com" + newsoup.find("div","sidearm-roster-player-image").find("img")["src"]
	name = firstName + "_" + lastName + ".jpg"
	imageFile = requests.get(image,headers={'User-Agent': 'Custom'},stream=True)
	output = open("OSU/image/"+name,"wb")
	for block in imageFile.iter_content(1024):
            if not block:
                break
            output.write(block)
	output.close()
	'''
	information = newsoup.find_all("dt")
	att = []
	att.append('firstName')
	att.append('lastName')
	for item in information:
		att.append(item.get_text())
	att.append('collegeNameShort')
	att.append('collegeNameFull')
	att.append('mascot')
	hit = ["hit_AVG", "hit_GP", "hit_GS", "hit_AB", "hit_R", "hit_H", "hit_2B", "hit_3B", "hit_HR", "hit_RBI", "hit_SLG%", "hit_BB", "hit_HBP", "hit_SO", "hit_GDP", "hit_OB%", "hit_SF", "hit_SH", "hit_SB", "hit_PO", "hit_A", "hit_E", "hit_FLD%"]
	att += hit
	pitch = ["pitch_ERA", "pitch_W", "pitch_L", "pitch_APP", "pitch_GS", "pitch_CG", "pitch_SHO", "pitch_SV", "pitch_IP", "pitch_H","pitch_R", "pitch_ER", "pitch_BB", "pitch_SO", "pitch_2B", "pitch_3B", "pitch_HR", "pitch_BF", "pitch_BAVG", "pitch_WP", "pitch_HBP", "pitch_BK", "pitch_SFA", "pitch_SHA"]
	att += pitch
	if(flag == 0):
		print(*att, sep=',', end='\n')
		flag += 1
	information1 = newsoup.find_all("dd")
	content = []
	content.append(firstName)
	content.append(lastName)
	for item in information1:
		content.append(item.get_text().replace(","," "))
	collegeName = ['OSU', 'Oregon State University', 'Beaver']
	content += collegeName
	stats = newsoup.find("section","sidearm-roster-player-stats")
	tables = stats.find_all("table")
	hit_stats = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	pitch_stats = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	if(len(tables) == 0):
		new_hit = []
		new_pitch = []
	else:
		new_hit = []
		new_pitch = []
		for subtable in tables:
			title = subtable.find("caption").get_text()
			if(title  == "Career Hitting Statistics"):
				tr = subtable.find_all("tr")
				for item in tr:
					if(item.find("th").get_text() == "Total"):
						for stat in item.find_all("td"):
							new_hit.append(stat.get_text())

			if(title == "Career Pitching Statistics"):
				tr = subtable.find_all("tr")
				for item in tr:
					if(item.find("th").get_text() == "Total"):
						for stat in item.find_all("td"):
							new_pitch.append(stat.get_text())

	if(new_hit == []):
		content += hit_stats
	else:
		content += new_hit
	if(new_pitch == []):
		content += pitch_stats
	else:
		content += new_pitch	
	print(*content, sep=',', end='\n')
driver.quit()
	



