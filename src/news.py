from BBCHeadlines import news

body = ''

def headlines():
  for article in news(limit=5):
    body = body + article['title'] + '.\n'
  return(body)