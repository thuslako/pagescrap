import re
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup

data          = []
categories    = []
titles        = []
names         = []
bodies        = []
urls          = []
auths         = []
morelinks     = []



driver = webdriver.Chrome("/chromebrowser/chromedriver")


def _check_link(line):
    match = re.search(r"(http[s]?:\/\/)(www\.)?(advocatedaily\.com).(.*)", line )
    if match:
        return match
    return None

def _parse_page(link):
    driver.get(link)
    content = driver.page_source
    soup = BeautifulSoup(content)
    for a in soup.findAll('section', attrs={'class':'article'}):
        
        category = a.find('strong', attrs={'data-child':'category'})
        title    = a.find('h1', attrs={'data-child':'headline'})
        auth     = a.find('strong', attrs={'data-child':'byline'})
        name     = a.find('h2', attrs={'class':'lawyer-names'})
        body     = a.find('div', attrs={'data-child':'body'})
        more     = a.find('p', attrs={'data-child':'read-more'})
        url      = link

        categories.append(category.text)
        titles.append(title.text)
        auths.append(auth.text)
        names.append(name.text)
        bodies.append(body)
        morelinks.append(more)
        urls.append(url)


    return None 

def parse_links(filepath):
    with open(filepath, 'r') as file_object:
        line = file_object.readline()
        while line:
            match = _check_link(line)
            # link = re.split(r"(advocatedaily\.com)?",line)
            if match:
                # url = re.split(r"(advocatedaily\.com)?",line)
                # url = re.search(r'(advocatedaily\.com)?',line)
                _parse_page(match.group(0))
                data.append(match.group(0))
                # print(match.group(0))
                
            # adv.append(link)
            line = file_object.readline()  


parse_links("list.txt")
df = pd.DataFrame({'Link Name':data})
df.to_csv('links.txt', index=False, encoding='utf-8')

dg = pd.DataFrame({'Title':titles,'name':names, 'auth':auths,'body':bodies,'more link':morelinks,'url':urls})
dg.to_csv('hull.csv', index=False, encoding='utf-8')




