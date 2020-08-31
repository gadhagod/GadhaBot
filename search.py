from googlesearch import search 

def gsearch(query):
	print('Google search query')
	results = ''
	for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
		results = results + j + '\n'
	return results 
