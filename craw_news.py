import requests, os
from bs4 import BeautifulSoup

Here = os.path.dirname(os.path.realpath(__file__))
Sub = "text"
page_source = "data_craw.txt"

max_articles = 30

# prepare 30 random articles from BBC news.

with open(os.path.join(Here,page_source)) as src:
    pages = src.readlines()
pages = [x.strip() for x in pages]


for each_page in pages:
    page = requests.get(each_page)
    page.encoding
    soup = BeautifulSoup(page.content, "html.parser")
    p = soup.find_all('p')

    file_name = each_page[24:]+".txt"
    print("=== reached: "+ each_page +" ===")
    article = open(os.path.join(Here,Sub,file_name),"w+",encoding='utf-8')

    for line in range(12,len(p)-10):
        # news article start from 12th <p> tag, get 22 p tag.
        text = p[line].get_text()
        print(text)
        article.write(text)
    article.close()
"""

url = "http://www.bbc.com/news/world-us-canada-42544605"
page = requests.get(url)
if page.status_code == 200:
    print("reached [",page.status_code,"] :",url)
    soup = BeautifulSoup(page.content, "html.parser")
    p = soup.find_all('p')

    #for id,each_p in enumerate(p):
    #    print(id," content:",each_p)

    for each_p in range(12,len(p)-10):
        print(p[each_p].get_text())

else:
    print("not reached [",page.status_code,"]")

"""
