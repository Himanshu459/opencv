import cv2

def empty():
    pass

path =r'C:\Users\Himanshu\PycharmProjects\OpencvPython\resources\lambo.jpg'
cv2.namedWindow("TrackBars")
cv2.resize("TrackBars",640,480)
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)


img= cv2.imread(path)
imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow("original",imgHSV)
cv2.imshow("original2",img)
cv2.waitKey(0)