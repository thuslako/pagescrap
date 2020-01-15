import urllib2
import pandas as pd 
from bs4 import BeautifulSoup

links = []
resp = urllib2.urlopen('http://hullandhull.com/news-events/')
soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))

# def _parse_link(link)
#     for key, rx in rx_dict.items():
#         match = rx.search(line)
#         if match:
#             links.append(match)


for link in soup.find_all('a', href=True):
    links.append(link['href'])

df = pd.DataFrame({'Link Name':links})
df.to_csv('products.txt', index=False, encoding='utf-8')
