import speech_recognition as sr 

class listern:
	def __init__(self,threshold):
		self.r = sr.Recognizer()
		self.m = sr.Microphone()
		self.r.energy_threshold = threshold
		self.r.dynamic_energy_threshold = False

	def to_Mic(self):
		with self.m as source:
			self.audio = self.r.listen(source)
			try:
				phrase = self.r.recognize_google(self.audio,language = "en-IN")
				return phrase
			except LookupError:	
				print("Oops! Didn't catch that")

	def recognize_voice(self,data_list,phrase):
		self.list1 = data_list
		self.phrase = phrase
		try:
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