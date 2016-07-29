
class classifier:

	categories=[]
	totalcategories={}
	words={}
	preferences={}

	def __init__(self,extractor,trainedset=None,features=None):
		if trainedset==None:
			self.trainedset={}
		else:
			self.trainedset=trainedset
		self.extractor=extractor

	def prepare(self,filename):
		for line in open(filename,'r').readlines():
			words=line.split()
			for word in words:
				wordprefs=word.split('/')
				if wordprefs[0] not in self.preferences.keys():
					self.preferences.update({wordprefs[0].lower(),int(wordprefs[1])})
	
	def train(self,filename):
		words=self.extractor(filename)
		for word in words:
			self.words.setdefault(word[0],0)
			self.words[word[0]]+=1
			self.__learn(word[0],word[1])

	def __learn(self,word,category):
		self.trainedset.setdefault(word,{})
		self.trainedset[word].setdefault(category,0)
		if category not in self.categories:
			self.categories.append(category)
		self.trainedset[word][category]+=1
		self.totalcategories.setdefault(category,0)
		self.totalcategories[category]+=1

	def getrating(self,word,category):
		try:
			return self.trainedset[word][category]
		except:
			return 0.1

	def getprob(self,sentence):
		words=[]
		prob={}
		for word in sentence.split():
			if word.lower() not in words:
				words.append(word.lower())
		changed=0
		for category in self.categories:
			prob.update({category:1})
			for word in words:
#				print word+' ',
#				print category
#				print self.getrating(word,category)
#				print self.totalcategories[category]
				try:
					prob[category]*=(float(self.getrating(word,category))/float(self.words[word]))
					changed=1
				except:
					prob[category]*=0.1
#				print ''
		answer=''
		probability=0
		for category,likelyhood in prob.iteritems():
			if likelyhood>probability:
				answer=category
				probability=likelyhood
		return answer,probability
		
			
			

	def display(self):
		print self.trainedset


	

