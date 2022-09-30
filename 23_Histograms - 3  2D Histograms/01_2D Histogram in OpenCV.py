import cv2
import numpy as np

img = cv2.imread('home.jpg')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])

cv2.imshow("img",hist)
cv2.waitKey(0)
cv2.destroyAllWindows()