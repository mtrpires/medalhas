#-*- coding: utf-8
import mechanize
import requests
from bs4 import BeautifulSoup
import csv

#go to main page
mech = mechanize.Browser()
base_url = "http://mail.olympicdb.com/"
# summer = "all-summer-olympiads.html"
# page = mech.open(base_url+summer)
# html = page.read()
#
# soup = BeautifulSoup(html)

years = [1896, 1900, 1904, 1908, 1912, 1920, 1924, 1928, 1932, 1936, 
    1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 
    1988, 1992, 1996, 2000, 2004, 2008]

# #get links for games
# links = soup.find_all('table')[1].find_all('a')
# links_url = []
# for l in links:
#     links_url.append(l.get('href'))

# print "Lista de jogos:", links_url

#go for games
for game in years:
    print "Going for", game
    print base_url+'United-States-{0}.html'.format(game)
    html = mech.open(base_url+'nation/United-States-{0}.html'.format(game)).read()
    soup = BeautifulSoup(html)
    tables = soup.find_all('table')
    for i in tables[2:]:
        rows = i.find_all('tr')
        data = []
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip().encode('utf8') for ele in cols]
            data.append([ele for ele in cols])
        with open('olydb.csv', 'a+') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(data)
    print "Tables saved!"