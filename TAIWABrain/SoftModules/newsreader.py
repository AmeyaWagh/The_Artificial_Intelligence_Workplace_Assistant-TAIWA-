from BeautifulSoup import *
import urllib2
import sys
import time
from TAIWABrain.Speech import speech
import TAIWABrain.utils as u
import os

class NewsFinder:
	headlines={}
	def __init__(self,urls):
		self.urls=urls
		self.S = speech('hindi')

	def surfPages(self):
		for url in self.urls:
			page=urllib2.urlopen(url)
			source=BeautifulSoup(page.read())
			self.__extractnews(source)
	
	def __extractnews(self,code):
		tags=code.findAll('item')
		for tag in tags:
			contents=tag.findChildren()
			self.headlines.update({contents[0].getText():contents[3].getText().split('&lt;')[0]})		

	def readnews(self):
		os.system('clear')
		for headline,description in self.headlines.iteritems():
			u.banner_open()
			print headline
			u.banner_close()
			self.S.say(headline)
			time.sleep(1)
			


if __name__=='__main__':
	urls=['http://timesofindia.feedsportal.com/c/33039/f/533921/index.rss']
	Reporter=NewsFinder(urls)
	Reporter.surfPages()
	Reporter.readnews()
