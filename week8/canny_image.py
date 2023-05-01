import cv2
import numpy as np

img = cv2.imread('s.jpg')
height, width, channel = img.shape
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 3)
canny = cv2.Canny(gray, 50, 150)
cframe = np.hstack((gray, sobel, canny))
cv2.imwrite('canny.jpg', cframe)


