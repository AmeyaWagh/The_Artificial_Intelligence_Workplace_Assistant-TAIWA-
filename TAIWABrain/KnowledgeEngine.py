import wolframalpha


class knowledgeEngine:
	def __init__(self):
		self.client = wolframalpha.Client('33UGAT-99UH9343K3')

	def get_knowledge(self,_query):
		self.result = self.client.query(_query)
		self.pod = self.result.pods[1]
		if self.pod.text:
			self.texts = self.pod.text
		else:
			self.texts = 'I have no answer for that'
		return self.texts		

if __name__ == '__main__':
	K = knowledgeEngine()
	while 1:
		ask = raw_input('ask a question')
		print K.get_knowledge(ask)