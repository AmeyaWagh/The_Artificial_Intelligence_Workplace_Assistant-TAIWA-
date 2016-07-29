import os
import speechreco as s
import if_speech
import speech_recognition as sr
import pickle
import thread
import TAIWABrain.utils as u

#---------------- DEFINITIONS ----------------------------------------------------
def recognise_face():
	workingdir = os.curdir
	print workingdir
	os.chdir("/home/ameya/FinalProjectBrain/face_Detection/")
	os.system("sudo python /home/ameya/FinalProjectBrain/face_Detection/face_recognition_nn.py")
	os.chdir(workingdir)

def who_am_I():
	usr = pickle.load(open('/usr/lib/python2.7/TAIWABrain/userprofile.user','rb'))
	print usr 
	S = if_speech.if_speech("hindi")
	S.speak("you are %s"%usr)

def play_song():
	os.system("sudo python songs_play.py")

def take_a_note():
	u.banner_open()
	os.system("sudo python dictation.py")
	u.banner_close()

def read_the_note():
	u.banner_open()
	fp = open('tempnote.txt','r')
	note = fp.readlines()
	for line in note: 
		S.speak(line)
	u.banner_close()	
		
def show_me_note():
	u.banner_open()
	os.system("cat tempnote.txt")
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
def kill_proc():
	os.system('sudo python pkill.py')
def main():
	usr = pickle.load(open('/usr/lib/python2.7/TAIWABrain/userprofile.user','rb'))

	S = if_speech.if_speech("hindi")
	S.speak("Hello sir!")


	r = sr.Recognizer()
	m = sr.Microphone()
	r.energy_threshold = 4000
	r.dynamic_energy_threshold = False
	print "A moment of silence please"

	while True:
		with m as source:
			try:
				audio = r.listen(source)
				phrase = r.recognize_google(audio)
				print 'Query:',
				print phrase
				print 'response'
				if "song" in phrase:
					thread.start_new_thread( play_song, () )
				elif "recognise" in phrase:
					thread.start_new_thread( recognise_face, () )
				elif ("who" in phrase) and ("am" in phrase) and ("I" in phrase):
					who_am_I()
				elif "note" in phrase:
					if "take"in phrase:	
						take_a_note()	
					elif "read" in phrase:
						read_the_note()	
					elif "show" in phrase:
						show_me_note()	
				elif (("get"or"show")and"email")in phrase:
					get_email()
				elif 'news' in phrase:
					todays_news()
				elif 'Google' in phrase:
					google_search(phrase)
				elif 'kill' in phrase:
					kill_proc()
					print 'killed successfully'
				elif "goodbye"	in phrase:
					S.speak("Goodbye! %s"%usr)
					quit()	
				else:
					print phrase
					pass
			except LookupError:
				print "something wrong"
				pass
			except KeyboardInterrupt:
				S.speak("Goodbye!")
				quit()

if __name__ == '__main__':
	main()					