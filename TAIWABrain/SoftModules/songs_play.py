import os
from TAIWABrain.Listern import listern
from TAIWABrain.Speech import speech
import thread
import sys

def PlaySong(_gana):
	os.system("mpg123 -q ./songs/"+_gana)

S = speech('hindi')
voice = listern(4000)
mysongs  = []
print "-------------------- SONGS ------------------------------------ "
songsDir = sys.argv[1]
print songsDir
songs = os.listdir(songsDir)
for i in range(len(songs)):
	print songs[i].lower().split('.')[0]
	mysongs.append(songs[i].lower().split('.')[0].replace(" ",""))
print " "
print "-------------------- SONGS ------------------------------------ "
S.say(" This is the list of songs . Which one should i play ")

while True:
	index = voice.recognize_voice(mysongs,voice.to_Mic())
	print songs[index].replace(" ", "\ ")
	S.say(" Playing ..." + (songs[index].replace(".mp3","")))
	gana = (songs[index].replace(" ","\ "))
	#PlaySong(gana)
	thread.start_new_thread( PlaySong,(gana,) )
	voice1 = listern(5000)
	while True:
		phrase = voice1.to_Mic()
		print phrase
		if 'stop' in phrase :
			S.say("closing songs")
			quit()



