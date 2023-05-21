import cv2
import numpy as np

# img = cv2.imread(input("Enter image file:"))
img = cv2.imread('circie_2.jpg')
# Thres = int(input("Enter canny threshold:"))


Thres = int(150)
dp = 1.2
minDist = 30

img2 = img.copy()
Y, Cr, Cb = cv2.split(cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb))
blur = cv2.GaussianBlur(Y, (3, 3), 0)
circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, dp, minDist, None, Thres)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        cv2.circle(img2, (i[0], i[1]), i[2], (0, 255, 0), 2)
        cv2.circle(img2, (i[0], i[1]), 2, (0, 0, 255), 5)

merged = np.hstack((img, img2))
cv2.imwrite('circle.jpg', merged)

