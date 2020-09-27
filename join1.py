import cv2
import numpy as np

path =r'C:\Users\Himanshu\PycharmProjects\OpencvPython\resources\lambo.jpg'
img= cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(imgGray)
imgBlank = np.zeros((512,512,3),np.uint8)
cv2.imshow("image",img)


cv2.imshow("temp",tmp)






imgHor = np.hstack((img,img))
imgver = np.vstack((img,img))

cv2.imshow("Horizontal",imgHor)
cv2.imshow("Vertical",imgver)

cv2.waitKey(0)