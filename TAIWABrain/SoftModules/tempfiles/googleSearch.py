import urllib
import json

searchurl = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q='
exampleSearch = 'leap motion sensor'
encodedData =urllib.quote(exampleSearch)
print encodedData

rawData = urllib.urlopen(searchurl+encodedData).read()
jsonData = json.loads(rawData)
searchResults = jsonData['responseData']['results']

for result in searchResults:
	title = result['title']
	link = result['url']
	print title
	print link
	print '''


	'''