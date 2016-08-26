# -*- coding: utf-8
import urllib2
import re
import csv
from bs4 import BeautifulSoup
import httplib

httplib.HTTPConnection._http_vsn = 10
httplib.HTTPConnection._http_vsn_str = 'HTTP/1.0'

base_url = 'http://www.sports-reference.com'

###pega links
def get_links(soup, selector):
    '''
    Get links from a soup using a specific selector
    soup: BeautifulSoup object
    selector: string
    return: list of links
    '''
    links = soup.select(selector)
    links = [link.get('href') for link in links]
    return links

def soupify(url):
    '''
    Creates an bs4 object with the contents of an URL
    url: string
    reeturn: bs4 object
    '''
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    return soup

#guarda o nome do país
def get_data(soup):
    '''
    Gets the name of the Country
    soup: BeautifulSoup object
    return: list (country, year, city)
    '''
    data = []
    h1 = soup.find_all('h1')[0].text
    match = re.search('(\w.+) at the (\d{4}) (\w.+) (\w.+) Games', h1)
    country = match.group(1).encode('utf8')
    year = match.group(2).encode('utf8')
    city = match.group(3).encode('utf8')
    kind = match.group(4).encode('utf8')
    data.extend((year, city, kind, country))
    return data

#guarda a tabela (pula primeira linha)
def get_table(soup, year, city, kind, country, selector_rows):
    '''
    Retrieves a specific table from a page using its selector
    soup: bs4 object
    selector_rows: string with the selector for the tr's of the table
    return: list (array) with header & rows
    '''
    # empty list that will hold the headers and a list of rows
    table = []
    rows_list = []
    rows = soup.select(selector_rows)
    header_text = rows[0].text
    # removes leading and trailing characters
    columns = header_text.split('\n')[1:-1]
    columns.extend(('Year', 'City', 'Type', 'Country'))
    table.extend((columns, rows_list))
    # skips first row
    for row in range(len(rows))[1:]:
        current_row = []
        for data in rows[row].select('td'):
            current_row.append(data.text.strip().encode('utf-8'))
        current_row.extend((year, city, kind, country))
        table[1].append(current_row)
    return table

#salva tabela
def save_table(table, flag):
    '''
    Saves table in the csv
    table: list
    flag: boolean
    '''
    with open('medalhas.csv', 'a') as f:
        writer = csv.writer(f)
        if flag:
            writer.writerow(table[0])
        writer.writerows(table[1])

def assert_table(soup):
    '''
    checks whether there is a table or not!
    soup: BeautifulSoup object
    return: True of False
    '''
    table = soup.select("#athletes tbody")
    check = len(table) > 0
    return check

def is_game(string):
    '''
    Determines wheter string contains "summer" or "winter"
    '''
    score = 0
    if "summer" in string:
        score += 1
    if "winter" in string:
        score += 1
    return score > 0

#entra na pagina de países, faz sopa, pega links_paises
url = "/olympics/countries/"
soup = soupify(base_url+url)
selector_paises = "#countries tbody a"
selector_rows = "#athletes tr"
links_paises = get_links(soup, selector_paises)

flag = True

#entra no país, faz sopa, pega links de jogos
for pais in links_paises:
    soup = soupify(base_url+pais)
    selector_jogos = "#medals tbody a"
    links_jogos = get_links(soup, selector_jogos)
#entra na página do ano, faz sopa, pega atletas
    for jogo in links_jogos:
        #entra no primeiro jogo
        if is_game(jogo):
            soup = soupify(base_url+jogo)
            print "Link:", jogo
            if assert_table(soup):
                year = get_data(soup)[0]
                city = get_data(soup)[1]
                kind = get_data(soup)[2]
                country = get_data(soup)[3]
                table = get_table(soup, year, city, kind, country, selector_rows)
                save_table(table, flag)
                flag = False
            else:
                print "No table at", country, year, city
                print "Last saved row:", table[1][-1]
    print country, "done."
print "all done."
