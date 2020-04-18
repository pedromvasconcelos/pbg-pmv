# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 20:40:31 2020

@author: pmesquit
"""

from bs4 import BeautifulSoup


import requests

headers = {
    'authority': 'en.wikipedia.org',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'sec-fetch-dest': 'document',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'accept-language': 'en,en-US;q=0.9,pt;q=0.8',
    'cookie': 'GeoIP=IE:L:Dublin:53.33:-6.25:v4; enwikimwuser-sessionId=668b5d652eb722880f95; WMF-Last-Access=06-Apr-2020; WMF-Last-Access-Global=06-Apr-2020',
}
def get_page_contents():
    response = requests.get('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population', headers=headers)
    return response.content


# Parse the html content
def convert_to_soup(content):
    return BeautifulSoup(content, 'html.parser')

#Find wikipedia table
def get_gdp_table(soup):
    return soup.find("table", attrs={"class": "wikitable"})

#Finding my data
def get_gdp_table_data(gdp_table):
    return gdp_table.tbody.find_all("tr")

#Th is where my headings are. I've created them in a list for later use of unittest
def heading(gdp_table_data):
    headings = [] 
    for th in gdp_table_data[0].find_all("th"):
        heading = (th.text.replace('\n', ''))
        headings.append(heading)
    return headings
    
#tr is where each row is
#td is each value for each row:
def data(gdp_table_data):
    for tr in gdp_table_data:
        for td in tr.find_all("td"):
            value = td.text.replace('\n', '').strip()
            if len(value) <= 3 or value == '-':
                print('\n', value, end=',')
            elif value[0:8] == 'National':
                print(value, end = ',')
            elif value[0].lower() in 'abcdefghijklmnopqrstuvwxyz<':
                print(value, end=',')
            else:
                print('"' + value + '"', end=',')
                
                
def main():                
    contents = get_page_contents()
    soup = convert_to_soup(contents)
    gdp_table = get_gdp_table(soup)
    gdp_table_data = get_gdp_table_data(gdp_table)
    print(str(heading(gdp_table_data)).strip('[]').replace("'",""),end='')
    data(gdp_table_data)
if __name__ == '__main__':
    main()                