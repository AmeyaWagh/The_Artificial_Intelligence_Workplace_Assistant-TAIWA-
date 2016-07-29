#----------------------------License---------------------------------------------------
#This project is created by: 
# Aditya Shinde <shinde.aditya386@gmail.com> 
# Aditya Bhopale<adityabhopale95@gmail.com>
# Ameya Wagh<ameya555@gmail.com>
# Onkar Ghone<onkar.ghone5@gmail.com>
#-------------------------------------------------------------------------------

import os
from TAIWABrain.Speech import speech
from TAIWABrain.Listern import listern
from TAIWABrain.lang import Main
from TAIWABrain.classifier import classifier
from TAIWABrain.KnowledgeEngine import knowledgeEngine
from TAIWABrain.HomeAutomation import homeautomation
from TAIWABrain.DoorLock import doorlock
import pickle
import thread

import TAIWABrain.utils as u

#----------------------------Initialisations---------------------------------------------------
sysPath = '/usr/lib/python2.7/TAIWABrain/'
modulePath = sysPath+'SoftModules/'
dataSetPath = sysPath+'data.csv'
S = speech('hindi')
voice = listern(4000)
bayesian=classifier(Main().extractor)
bayesian.train(dataSetPath)
M=Main()
K = knowledgeEngine()
home = homeautomation()
door = doorlock()
#----------------------------Definitions-------------------------------------------------------
def recognise_face():
	RecoPath = modulePath+'faceRecognition'
	os.chdir(RecoPath)
	os.system("sudo python face_recognition_nn.py")
	os.chdir(modulePath)
	usr = pickle.load(open(sysPath+'userprofile.user','rb'))
	S.say("Welcome %s"%usr)

def read_ocr():
	os.system('sudo python ocr_reader.py')

def who_am_I():
	usr = pickle.load(open(sysPath+'userprofile.user','rb'))
	print usr 
	S.say("you are %s"%usr)

def play_song():
	songPath = './songs'
	os.system("sudo python songs_play.py "+songPath)

def take_a_note():
	u.banner_open()
	os.system("sudo python dictation.py")
	u.banner_close()

def read_the_note():
	u.banner_open()
	fp = open('tempnote.txt','r')
	note = fp.readlines()
	for line in note:
		print line 
		S.say(line)
	u.banner_close()

def show_me_note():
	u.banner_open()
	os.system("cat tempnote.txt")
	os.system("sudo python sample.py tempnote.txt")
	u.banner_close()

def mail_sender():
	u.banner_open()
	os.system("sudo python mailer.py")
	u.banner_close()

def get_email():
	os.system('sudo python get_mail_inbox.py')

def todays_news():
	os.system('sudo python get_news.py')

def google_search(searchTerm):
	searchTerm = searchTerm.replace('Google','')
	searchTerm = searchTerm.replace(' ','+')
	print searchTerm
	os.system('sudo python GoogleSearch.py %s'%searchTerm)	

def process_routine(_task):
	if _task == 'greetings':
		S.say("Hello")
	elif _task == 'news':
		todays_news()
	elif _task == 'note':
		take_a_note()
	elif _task == 'Email':
		get_email()
	elif _task == 'Rnote':
		show_me_note()
		read_the_note()
	elif _task == 'Login':
		recognise_face()
	elif _task == 'song':
		play_song()
	elif _task == 'fan ON':
		print 'fan ON'
		home.fan_on()
	elif _task == 'fan OFF':						
		print 'fan OFF'
		home.fan_off()
	elif _task == 'light ON':
		print 'light ON'
		home.light_on()
	elif _task == 'light OFF':
		print 'light OFF'
		home.light_off()
	elif _task == 'whoAmI':
		who_am_I()
	elif _task == 'camera':
		os.system('sudo python camera_feed.py')
	elif _task == 'lock':
		door.lock()
	elif _task == 'unlock':
		door.unlock()
	elif _task == 'mailer':
		mail_sender()
	elif _task == 'ocr':
		read_ocr()
	elif _task == 'goodbye':
		usr = pickle.load(open(sysPath+'userprofile.user','rb'))
		S.say("Goodbye! %s"%usr)
		quit()				
	else:
		print 'I did not understand the task'		
	
def main():
	print sysPath
	os.chdir(modulePath)
	os.system('pwd')
	usr = pickle.load(open(sysPath+'userprofile.user','rb'))
	print usr
	print "A moment of silence please"
	while True:
		try:
			phrase = None
			try:
				while phrase == None:
					phrase = voice.to_Mic()
					if phrase == None:
						S.say("Sorry, I didn't get that. Try again")
						print "Sorry, I didn't get that. Try again"
			except KeyboardInterrupt:
				S.say("Goodbye! %s"%usr)
				quit()	
			os.system('clear')
			print 'Query:',
			print phrase
			print 'response'
			
			sentiment =  M.sent_identifier(phrase)
			bias =  M.biasing(phrase)

			if sentiment == 'question':
				print phrase+'?'
				try:
					result = K.get_knowledge(phrase)
					print 'answer: '+result
					S.say(result)
				except LookupError:
					print "Wolfram couldn't find"
					google_search(phrase)	

			elif sentiment == 'assertion':	
				answer,acc=bayesian.getprob(phrase)
				print answer+' ',acc
				process_routine(answer)

		except LookupError:
			print "something wrong"
			pass
		except KeyboardInterrupt:
			#S.say("Goodbye!")
			quit()
#---------------------------Execution-----------------------------------------------------------
if __name__ == '__main__':
	main()	
