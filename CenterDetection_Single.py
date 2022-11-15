import cv2
import numpy as np
from matplotlib import pyplot as plt

#need to create a test image to be sample4
img = cv2.imread("Media/Test1_Sample4.jpg", 0)

#originalWidth = img.shape[1]
#originalHeight = img.shape[0]
#x1 = int(originalWidth*(68/128))
#x2 = int(originalWidth*(70/128))
#y1 = int(originalHeight*(4/8))
#y2 = int(originalHeight*(5/8))

#cropped_img = img[y1:y2, x1:x2]

#monoImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
monoImage2 = cv2.Canny(img, 50, 200)
ret, thresh = cv2.threshold(monoImage2, 127, 255, 0)
moments = cv2.moments(thresh)
xCenter = int(moments["m10"] / moments["m00"])
yCenter = int(moments["m01"] / moments["m00"])
cv2.circle(monoImage2, (xCenter, yCenter), 2, (255, 255, 255), -1)

cv2.imshow('New_Frame', monoImage2)
cv2.waitKey(0)
cv2.destroyAllWindows()