import smtplib
#--------------------------------------
from TAIWABrain.Listern import listern
from TAIWABrain.Speech import speech

S = speech('hindi')
voice = listern(4000)
S.say('Whom should I mail this?')
contacts = {'Aditya':'adityabhopale95@gmail.com','Omkar':'onkar.ghone5@gmail.com','aditya':'adityabhopale95@gmail.com','omkar':'onkar.ghone5@gmail.com','ashish':'ashishharsola@gmail.com','Ashish':'ashishharsola@gmail.com'}
phrase = voice.to_Mic()
print phrase
for contact in contacts.keys():
	if contact in phrase:
		yourEmail = contacts[contact]
		S.say('Sending this mail to' + contact)

fp = open('tempnote.txt','r')
myemail = "fcritextc.group4@gmail.com"
mypassword = "ArtificialIntelligence"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(myemail,mypassword)
msgs = fp.readlines()
tempmsg = ''
for msg in msgs:
	tempmsg = tempmsg + msg
print tempmsg
server.sendmail(myemail,yourEmail, tempmsg)
server.quit()
print 'done'
S.say('Mail sent!!')