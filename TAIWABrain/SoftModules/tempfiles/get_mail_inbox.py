import imaplib
import email
import os
from TAIWABrain.Speech import speech
#------------------------------------------------------

os.system("clear")
S = speech('hindi')
def banner(_str,_symbol):
	print '\n' 
	print _symbol*20 , _str ,_symbol*50
	print '\n' 

def txtfile_generator(msg):
	os.system('rm -f textnote.txt')
	os.system('touch textnote.txt')
	fp = open('textnote.txt','w')
	fp.write(msg)
	fp.close()

myemail = "agnelrobocon2014@gmail.com"
mypassword = "technovillain"

#------------------------------------------------------
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(myemail, mypassword)
mail.list()
# Out: list of "folders" aka labels in gmail.
mail.select("inbox") # connect to inbox.

result, data = mail.search(None, "ALL")

ids = data[0] # data is a list.
id_list = ids.split() # ids is a space separated string


latest_email_id = id_list[-1] # get the latest

result, data = mail.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID

raw_email = data[0][1] # here's the body, which is raw text of the whole email
# including headers and alternate payloads
raw_email_string = raw_email.decode('utf-8')
email_message = email.message_from_string(raw_email_string)

banner('NEW EMAIL ','#')
print 'Subject: ',email_message['subject']
print 'From: ',email_message['from']
banner('THE MESSAGE:','~')

S.say('You have a new Mail from %s'%(email_message['from'].split('<')[0]))
S.say('On the subject: %s'%email_message['subject'])
for part in email_message.walk():
	if part.get_content_type() == "text/plain": # ignore attachments/html
		#print part.keys()
		body = part.get_payload(decode=True)
		msg = body.decode('utf-8')
		#print (msg)
		txtfile_generator(msg)
		os.system('python sample.py')
		#S.say('It says!')
		#S.say(msg)
banner('END','#')  
