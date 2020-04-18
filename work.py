import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

base_url = 'https://www.mobygames.com/search/quick?'

queries =  ['Americas army : rise of a soldier Playstation 2', 'army men sage heros nintendo 64', 'Busy Scissors [Redken 5th Avenue NYC Presents]']


all_links = {}
all_info = {}

for query in queries:
    payload = {'q' : query, 'sFilter' : '1', 'sG' : 'on'}
    address = requests.get(base_url, params = payload)
    html = requests.get(address.url).text
    soup = BeautifulSoup(html, features="html.parser")
    result1 = soup.find_all('div', {'class' :'searchTitle'})
    main_links = []
    for element in result1:
        main_links.append(element.find('a')['href'])
    sub_links = []
    for a in soup.select('span[style="white-space: nowrap"] a[href]'):
        sub_links.append(a['href'])
    all_links[query] = main_links + sub_links
    result2 = soup.find_all('div',{'class':'searchData'})
    names = []
    for element in result2:
        names.append(element.text)
    all_info[query] = names
    

print(all_links)
print(all_info)


    
   
