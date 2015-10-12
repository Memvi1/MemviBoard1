import numpy as np
import cv2

cap=cv2.VideoCapture(0)

#fourcc = cv2.VideoWriter_fourcc(*'XCID')
#out= cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
out = cv2.VideoWriter('/media/sdcard/timer.avi',cv2.cv.CV_FOURCC('M','J','P','G'), 6.3, (640,480))
#out = cv2.VideoWriter('output.avi', -1, 20.0, (640,480))

#while(cap.isOpened()):
for i in range(1,100):
	ret, frame = cap.read()
	if ret:
		i=i+1
		out.write(frame)

#		cv2.imshow('Video Stream', frame)

	else:
		break

cap.release()
out.release()
cv2.destroyAllWindows() 





