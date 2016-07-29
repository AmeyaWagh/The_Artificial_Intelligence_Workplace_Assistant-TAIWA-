import os
import cv2
cap = cv2.VideoCapture(1)
while True:
	ret,img = cap.read()
	cv2.imshow('document',img)
	k = cv2.waitKey(5)
	print k
	if k == 1048689:
		break
	if k == 1048673:
		cv2.imwrite('image_ocr.tif',img)
		print 'Saving Image...'
		break
cap.release()
cv2.destroyAllWindows()
#os.system('export TESSDATA_PREFIX=~/Documents/final_project/jTessBoxEditor/tesseract-ocr/tessdata/')		
os.system('rm -f tempnote.txt')
os.system('tesseract image_ocr.tif tempnote')
os.system('cat tempnote.txt')
