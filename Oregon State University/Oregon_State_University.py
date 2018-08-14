import csv
import requests
from bs4 import BeautifulSoup

page = requests.get('https://osubeavers.com/roster.aspx?roster=159&path=baseball', headers={'User-Agent': 'Custom'})
html = page.text

newsoup = BeautifulSoup(html, "html.parser")
name = newsoup.find_all("td", "sidearm-table-player-name")

flag = 0

for item in name:
    newurl = "https://osubeavers.com/" + item.a.get("href")
    personalPage = requests.get(newurl, headers={'User-Agent': 'Custom'})
    temp = personalPage.text

    newsoup = BeautifulSoup(temp, "html.parser")
    names = newsoup.find("span", "sidearm-roster-player-name")
    firstName = names.find_all("span")[0].get_text()
    lastName = names.find_all("span")[1].get_text()

    image = "https://osubeavers.com/" + newsoup.find("div", "sidearm-roster-player-image").find("img")["src"]
    name = firstName + "_" + lastName + ".jpg"
    imageFile = requests.get(image, headers={'User-Agent': 'Custom'}, stream=True)
    output = open("OSU/image/" + name, "wb")

    for block in imageFile.iter_content(1024):
        if not block:
            break
        output.write(block)
    output.close()

    information = newsoup.find_all("dt")
    att = []
    att.append('firstName')
    att.append('lastName')
    for item in information:
        att.append(item.get_text())
    if (flag == 0):
        print(*att, sep=',', end='\n')
        flag += 1
    information1 = newsoup.find_all("dd")
    content = []
    content.append(firstName)
    content.append(lastName)
    for item in information1:
        content.append(item.get_text())
    print(*content, sep=',', end='\n')
