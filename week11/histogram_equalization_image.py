import cv2
import numpy as np


img = cv2.imread('dog.jpg')
t_frame = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
Y, Cr, Cb = cv2.split(t_frame)
Y_ = cv2.equalizeHist(Y)
merged = cv2.cvtColor(cv2.merge((Y_, Cr, Cb)), cv2.COLOR_YCrCb2BGR)

cimg = np.hstack((img, merged))
cv2.imwrite('Histogram_sky.jpg', cimg)
cv2.imwrite('weather_.jpg', merged)

