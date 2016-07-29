import os
from TAIWABrain.Listern import listern
from TAIWABrain.Speech import speech

#---------------------------------------
S = speech('hindi')
voice = listern(3000)
text = ""
phrase = ""
os.system("rm -f tempnote.txt")
fp = open('tempnote.txt','w')
#---------------------------------------
S.say('Starting note')
while True:
	try:
		phrase = voice.to_Mic()
		if phrase is not None:
			pass
		if ('next' and 'line') in phrase:
			text+= "\n"
			pass
		elif ('full' and 'stop') in phrase:
			text+= "."
			pass	
		elif ('close' and 'note') in phrase:
			break	
		else:		
			text+=phrase
			text+= " "
			print phrase
	except LookupError:
		print "Oops i didnt catch that"
	except KeyboardInterrupt:
		S.say('note closed')		
		print phrase
		fp.write(text)
		fp.close()
		quit()
S.say('note closed')		
print phrase
fp.write(text)
fp.close()
quit()		