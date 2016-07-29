from gtts import gTTS
import os

class speech:
	lang={'english':'en','hindi':'hi'}
	def __init__(self,lang='english'):
		self.language=self.lang[lang]

	def say(self,sentence):
		audio=gTTS(text=sentence,lang=self.language)
		audio.save(".temp.mp3")
		os.system("mpg123 -q .temp.mp3")
		self.__cleanup()

	def __cleanup(self):
		os.system('rm .temp.mp3')

		