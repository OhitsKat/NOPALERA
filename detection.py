import cv2
import serial
import time

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
nopalClassif = cv2.CascadeClassifier('cascade.xml')

arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)

def read_detection(x):
	arduino.write(bytes(x, 'utf-8'))
	time.sleep(10)

while True:
	detection = ''
	ret,frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	toy = nopalClassif.detectMultiScale(gray,
	scaleFactor = 3,
	minNeighbors = 100,
	minSize=(30000,30000))

	for (x,y,w,h) in toy:
		cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)
		cv2.putText(frame,'Nopal',(x,y-10),2,0.7,(0,0,255),2,cv2.LINE_AA)
		detection = 'open'

	if detection == 'open':
		read_detection("1")

	cv2.imshow('frame',frame)
	
	if cv2.waitKey(1) == 27:
		break
cap.release()
cv2.destroyAllWindows()