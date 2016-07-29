import classifier
import nltk

class Main:
	preferences=['VBP','VB','NN','NNS','VBG','RB','IN','VBD','JJ','VBN']
	def __init__(self):
		pass

	def extractor(self,filename):
		fhandle=open(filename,'r')
		info=[]
		for line in fhandle.readlines():
			linelist=line.strip().split(',')
			category=linelist[-1]
#			print "category"
#			print category
			words=' '.join(linelist[:-1]).split()
			taggedwords=nltk.pos_tag(words)
#			print taggedwords
			for word in taggedwords:
				if word[1] in self.preferences:
					info.append((word[0].lower(),category))
#		print info			
		return info

	def sent_identifier(self,_sent):
		_whType = ['which','what','who','when','where','why','how','whose','whom','is','are','will','can','could','would']
		_word_tokenised = nltk.word_tokenize(_sent)
		if _word_tokenised[0] in _whType:
			return 'question'
		else:
			return 'assertion'	

	def biasing(self,_sent):
		state = 1
		mag = 1

		resultant = 0

		#stopWords = set(stopwords.words('english'))

		_dict_extent = {'too':'inc','very':'inc','lot':'inc','less':'dec','meager':'dec','little':'dec'}
		_dict_bias = {'on':'pos','off':'neg','no':'neg','not':'neg','donot':'neg','never':'neg'}
	
		sent_tokenised = nltk.sent_tokenize(_sent)
		word_tokenised = []
		for sent in sent_tokenised:
			word_tokenised.append(nltk.word_tokenize(sent))
	
		for w_tokenised in word_tokenised:		
			for w in w_tokenised:
				if w in _dict_bias.keys():
					if 'neg' in _dict_bias[w]:
						state *= -1
					if 'pos' in _dict_bias[w]:
						state *= 1	
				if w in _dict_extent.keys():
					print _dict_extent[w]
					if 'inc' in _dict_extent[w]: 
						mag += 1 
					elif 'dec' in _dict_extent[w]:
						mag -=	1		
		print state
		print mag

		resultant = state*mag

		if resultant > 0 :
			return 'positive'
		elif resultant == 0:
			return 'neutral'
		else :
			return 'negative'	
				

if __name__=='__main__':
	bayesian=classifier.classifier(Main().extractor)
	bayesian.train('data.csv')
	while 1:
		answer,acc=bayesian.getprob(raw_input('- '))
		print answer+' ',
		print acc
	#bayesian.display()

