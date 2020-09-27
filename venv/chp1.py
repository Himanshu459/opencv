import numpy as np
import imutils
import cv2

#path = r'C:\Users\Himanshu\Desktop\test.mp4'
#video=cv2.imread(path)
#cap= cv2.VideoCapture("C:/Users/Himanshu/PycharmProjects/OpencvPython/resources/test.mp4")
url='http://192.168.0.104:8080/video'

cap = cv2.VideoCapture(url)
fps = int(cap.get(40000))
#cap.set(3,640)
#cap.set(4,480)
#cap.set(10,100)
while (True):
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=450)
    if frame is not None:
        cv2.imshow('frame',frame)
    q=cv2.waitKey(1)
    if q == ord("q"):
        break
cv2.destroyAllWindows()