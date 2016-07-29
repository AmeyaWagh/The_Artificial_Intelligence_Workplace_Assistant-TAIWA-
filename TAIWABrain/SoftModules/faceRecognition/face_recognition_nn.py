import sys
import pickle
import numpy as np
import cv2
#sys.path.append('/home/ameya/FinalProjectBrain')
import machinebrain

usr = pickle.load(open('/usr/lib/python2.7/TAIWABrain/userprofile.user','rb'))

net = pickle.load(open('trainednet1k.nn','rb'))
face_cascade_frontal = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
iface = []
faces = []
i = 0
person={2:'Ameya',1:'Shinde',0:'Bhopale'}
count_usr = []
usr_index = [0,0,0]
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
	ret,img = cap.read()
	
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
	gray = clahe.apply(gray)
	
	cv2.imshow('capture',gray)
	
	faces = np.array(faces)
	faces = face_cascade_frontal.detectMultiScale(gray, 1.3, 5)
	
	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]

		#print x,y
		
		iface = img[y:y+h, x:x+w]
		iface1 = cv2.resize(iface,(28,28))
		cv2.imshow('img3',iface1)
		
		iface1 = cv2.cvtColor(iface1,cv2.COLOR_BGR2GRAY)
		iface1 = iface1.reshape(784,)/255.00
		pred=net.predict(np.array([iface1]))[0]
		pred=(pred/max(pred)).tolist()
		count_usr.append(pred.index(1))
		iden=person[pred.index(1)]		
		cv2.putText(img,str(iden),(x,y+h+20), font, 1,(255,255,255),2,cv2.CV_AA)
		i=i+1
		
	
	cv2.imshow('img2',img)     
	k = cv2.waitKey(10)
	if i == 20:
		for x in count_usr:
			usr_index[x] = count_usr.count(x)
		final_usr = usr_index.index(max(usr_index))
		usr = str(person[final_usr])
		pickle.dump(usr,open('/usr/lib/python2.7/TAIWABrain/userprofile.user','wb'))
		print usr 
		break
	if k == ord('a') & 0xFF:
		break

cap.release()    
cv2.destroyAllWindows()
quit()
