# These code snippets use an open-source library.
import unirest

words = []
words = ['testing', 'incredible', 'awesome']

for x in words:
	print x

	response = unirest.get("https://wordsapiv1.p.mashape.com/words/" 
		+ x
		+ "/definitions",
	  headers={
	    "X-Mashape-Key": "IQopnvYrCnmsh9YYpnilUIvXqhO9p1XoYFcjsnry4tc16LDNtP",
	    "Accept": "application/json"
	  }
	)

	print response.body

response.body