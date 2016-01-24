#Gets the latest publications on my favorite
#scientific topics on PubMed. Just edit the search
#queries below to whatever you're interested in 
#and it'll give you a list of articles to quickly glance
#over the titles/authors/journal/date of.

import requests
from bs4 import BeautifulSoup

BASE_URL = 'http://www.ncbi.nlm.nih.gov/pubmed/?term='

queries = { 'dopamine fast scan cyclic voltammetry',
            'dopamine optogenetics',
            'model free decision making',
            'empathy rats',
            'set shifting',
            'in vivo electrophysiology',
            'artificial neural network',
            }

visited_titles = set() #used to avoid adding duplicate articles
articles = [] #list of dictionaries of articles

for query in queries:
    query.replace(" ", "+")
    html = requests.get(BASE_URL + query)
    soup = BeautifulSoup(html.text, "html.parser")
    result_set = soup.findAll("div", {"class" : "rslt"})
    for tag in result_set:
        title = tag.find('p', {'class' : 'title'}).text
        if title not in visited_titles:
            visited_titles.add(title)
            articles.append( {'title':title.encode('utf-8'),
                              'authors': tag.find('p', {'class' : 'desc'}).text.encode('utf-8'),
                              'details' : tag.find('p', {'class' : 'details'}).text.encode('utf-8'),
                              'keyword' : query
                              })
            
text = "Search results:\n"
for a in articles:
    text += "\n" + "%s\n%s\n%s\n%s\n\n" % (a['keyword'], a['title'], a['authors'], a['details'])


print(text)
print("Enjoy!\nPress Enter to exit.")
input()


        


