import cv2
import numpy as np

path =r'C:\Users\Himanshu\PycharmProjects\OpencvPython\resources\shapes.jpg'
img = cv2.imread(path)


def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    imgSize = np.zeros_like(img)
    imgContour = img.copy()
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            cv2.imshow("imgContour",imgContour)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            object = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour,(x,y),(x+w+y+h)),(0,255,0))

imgGray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)

im_v = cv2.vconcat([imgGray, imgBlur,])
im_v2 = cv2.vconcat([imgCanny, imgBlur,])

getContours(imgCanny)



cv2.imshow('shape0.0', im_v)
cv2.imshow('shape0.1', im_v2)

#cv2.imshow('shape0.3',)



cv2.waitKey(0)