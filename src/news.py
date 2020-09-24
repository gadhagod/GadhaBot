import feedparser
import requests
from bs4 import BeautifulSoup

BBC_FEED = "http://feeds.bbci.co.uk/news/world/rss.xml"

def parse_article(article_url):
  r = requests.get(article_url)
  soup = BeautifulSoup(r.text, "html.parser")
  ps = soup.find_all('p')
  text = "\n".join(p.get_text() for p in ps)
  return text

def headlines(strarticles):
  if strarticles == '':
    articles = 5
  else:
    articles = int(strarticles)  
  feed = feedparser.parse(BBC_FEED)
  article_texts = ""

  for article in feed['entries'][:articles]:
    title = article['title']
    article_texts = article_texts + title + '.\n'
        
  print('News query')
  return article_texts
