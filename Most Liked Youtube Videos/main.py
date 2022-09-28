from bs4 import BeautifulSoup
import pandas
import requests

url='https://en.wikipedia.org/wiki/List_of_most-liked_YouTube_videos'
req_url=requests.get(url)
req_url.raise_for_status()
soup=BeautifulSoup(req_url.content,'html.parser')
lists=soup.find_al ('table',class_='wikitable sortable jquery-tablesorter')
print(Lists)