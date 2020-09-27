import cv2
import numpy as np
path = r'C:\Users\Himanshu\PycharmProjects\OpencvPython\resources\picture.jpg'



def stackImage(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0],list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range (0,rows):
            for y in range(0,cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y],(0,0), None,3)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y],(imgArray[0][0]))
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]=cv2.cvtColor(imgArray)
        imageBlank = np.zeros((height,width,3),np.uint8)
        hor=[imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0,rows):
            hor[x] = np.hstack(imgArray[x])
        ver= np.vstack(hor)
    else:
        for x in range(0,rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x]=cv2.resize(imgArray[x],(0,0),None,scale,scale)
            else:
                imgArray[x]= cv2.resize((imgArray[x],(imgArray[0].shape[1]))
            #if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgStack)
        hor = np.hstack(imgArray)
        ver= hot
    return ver

img = cv2.imread(path)
imgStack =stackImage(0.5,([img,img,img]))

cv2.imshow("imageSttack",imgStack)





#path = r'C:\Users\Himanshu\PycharmProjects\OpencvPython\resources\picture.jpg'
#img = cv2.imread(path)

#imghor = np.hstack((img, img))
#imgvar = np.vstack((img, img))

#cv2.imshow("Horizontal", imghor)
#cv2.imshow("vartical", imgvar)
cv2.waitKey(0)
