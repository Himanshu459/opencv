import cv2
import numpy as np

path =r'C:\Users\Himanshu\PycharmProjects\OpencvPython\resources\obama.jpg'
img= cv2.imread(path)
width,height=250,350
pts1=np.float32([[113,6],[227,11],[111,128],[235,128]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix= cv2.getPerspectiveTransform(pts1,pts2)

imgOutput=cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow("image",img)
cv2.imshow("imagwarp",imgOutput)


cv2.waitKey(0)