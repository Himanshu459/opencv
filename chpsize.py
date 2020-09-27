import cv2


path =r'C:\Users\Himanshu\PycharmProjects\OpencvPython\resources\lambo.jpg'
img= cv2.imread(path)
#print(img.shape)

imageResize= cv2.resize(img,(1000,500))
imgCropped=img[0:100,100:300]

cv2.imshow("image",img)
cv2.imshow("imageResize",imageResize)
cv2.imshow("imageCroped",imgCropped)
cv2.waitKey(0)