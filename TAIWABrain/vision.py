import cv2
import numpy as np 

class faceRecognition:
	
	def __init__(self):
		self.face_cascade_frontal = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#		self.faces = faces
#		self.iface = iface
	def getface(self,img):
#		faces = np.array(self.faces)
#		iface = np.array(self.iface)
		iface = []
		self.img = img
		self.iface = iface
		self.img = np.asarray(self.img)
		slef.gray = cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)
		
		self.faces = self.face_cascade_frontal.detectMultiScale(self.gray, 1.3, 5)
		return gray
#		for (x,y,w,h) in faces:
#			return (x,y,w,h)
#			print (x,y,w,h)
#			iface = gray[y:y+h, x:x+w]
#			iface = cv2.resize(iface,(28,28))
#		return gray

	def getLBPHimg(self,img):
		self.img = img
		self.newImg = np.copy(self.img)
		self.img = cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)
		row,col = (self.img).shape
		self.hist = [0. for i in range(256)]
		self.hist = np.asarray(self.hist,dtype = 'uint8')
		for r in range(1,row-1):
			for c in range(1,col-1):
				self.temp = self.img[r,c]
				self.bin_val = 0
				self.bin_val = self.bin_val + 1*int(self.img[r,c-1]>self.temp)
				self.bin_val = self.bin_val + 2*int(self.img[r+1,c-1]>self.temp)
				self.bin_val = self.bin_val + 4*int(self.img[r+1,c]>self.temp)
				self.bin_val = self.bin_val + 8*int(self.img[r+1,c+1]>self.temp)
				self.bin_val = self.bin_val + 16*int(self.img[r,c+1]>self.temp)
				self.bin_val = self.bin_val + 32*int(self.img[r-1,c+1]>self.temp)
				self.bin_val = self.bin_val + 64*int(self.img[r-1,c]>self.temp)
				self.bin_val = self.bin_val + 127*int(self.img[r-1,c-1]>self.temp)
				self.newImg[r,c] = self.bin_val
				self.hist[self.bin_val] +=1
		return	self.newImg, self.hist 
