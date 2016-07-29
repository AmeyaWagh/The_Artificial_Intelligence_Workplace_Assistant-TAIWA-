import speech_recognition as sr

class speech_to_text:
	def __init__(self,threshold):
		self.r = sr.Recognizer()
		self.m = sr.Microphone()
		self.r.energy_threshold = threshold
		self.r.dynamic_energy_threshold = False
		print "A moment of silence please"

	def recognize_voice(self,data_list):
		self.list1 = data_list
		with self.m as source:
			print("Set minimum energy threshold to {}".format(self.r.energy_threshold))
			self.audio = self.r.listen(source)
			print "Got it....recognizing!!"
			phrase = self.r.recognize_google(self.audio)
			try:
				phrase = self.r.recognize_google(self.audio)
				extr = phrase.lower().split()
				join_word = "".join(extr)
				flag = 0
				for everyEle in self.list1:
					if everyEle in join_word:
						flag = 1
						common_word = everyEle
				if flag == 1:		
					return self.list1.index(common_word)
			except LookupError:
				print("Oops! Didn't catch that")
