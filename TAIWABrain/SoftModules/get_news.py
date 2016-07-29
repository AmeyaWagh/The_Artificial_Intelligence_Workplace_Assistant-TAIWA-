from bs4 import BeautifulSoup
import requests
import time
import newsreader
import os
from TAIWABrain.Listern import listern
from TAIWABrain.Speech import speech

S = speech('hindi')
voice = listern(4000)

def main():
	os.system('clear')
	S.say('Todays news:')
	main = "http://timesofindia.indiatimes.com/rss.cms"
	a = requests.get(main)
	soup = BeautifulSoup(a.text,'html.parser')
	soup1 = soup.find_all('table')
	soup2 =  soup1[1].find_all('table')
	soup3 = soup2[1].find_all('tr')
	i = 1
	link = []
	data_list = []
	for everyEle in soup3:
		news_type = everyEle.text.replace('More','')
		link.append(everyEle.a['href'])
		news_type1 = news_type.lower().split()
		data_list.append("".join(news_type1))
		print str(i) + ') ' + news_type
		i = i+1
	
	S.say('What type of news are you interested in?')

	news = None
	while news == None:
		news = voice.recognize_voice(data_list,voice.to_Mic())
		if news == None:
			S.say("Sorry, I didn't get that. Try again")
			print "Sorry, I didn't get that. Try again"

	new_url = link[news]
	new_url = [new_url]
	Reporter = newsreader.NewsFinder(new_url)
	Reporter.surfPages()
	Reporter.readnews()

if __name__ == '__main__':
	main()