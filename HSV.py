import cv2
import numpy as np




def empty(a):
    pass

path =r'C:\Users\Himanshu\PycharmProjects\OpencvPython\resources\lambo2.jpg'
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars" ,640,240)
cv2.createTrackbar("Hue Min" ,"TrackBars",0,179,empty)
cv2.createTrackbar("Hue Max" ,"TrackBars",179,179,empty)
cv2.createTrackbar("sat Min" ,"TrackBars",0,255,empty)
cv2.createTrackbar("sat Max" ,"TrackBars",255,255,empty)
cv2.createTrackbar("val Min" ,"TrackBars",0,255,empty)
cv2.createTrackbar("val Max" ,"TrackBars",255,255,empty)

while True:
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("val Max", "TrackBars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResult= cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow("Original",img)
    cv2.imshow("HSV",imgHSV)
    cv2.imshow("Mask",mask)
    cv2.imshow("Result",imgResult)
    #imgStack = stackImages(0.6,([img,imgHSV],[mask,imgResult]))
    #cv2.imshow("Stack images",imgStack)

    cv2.waitKey(1)