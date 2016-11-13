# Unirest is an open-source library I use for the WordsAPI at https://market.mashape.com/lisamschachtschneider/applications/gre-flashcards/charts/requests.
import unirest

words = []
words = ['testing', 'incredible', 'awesome']

for x in words:
	# print x

	response = unirest.get("https://wordsapiv1.p.mashape.com/words/" 
		+ x
		+ "/definitions",
	  headers={
	    "X-Mashape-Key": "IQopnvYrCnmsh9YYpnilUIvXqhO9p1XoYFcjsnry4tc16LDNtP",
	    "Accept": "application/json"
	  }
	)

	# print response.body

	definitions = response.body

	#convert to string
	# str(definitions)


	file = open("definitions.txt", "a")

	# file.write(test)
	# print definitions, 'definitions last'

	#pastes the last definition in the text file
	file.write(str(definitions))
