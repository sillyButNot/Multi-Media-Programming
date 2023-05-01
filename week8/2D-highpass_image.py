import cv2
import numpy as np



img = cv2.imread('s.jpg')
height, width, channel = img.shape

k_lap = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
k_lap_e = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
t_frame = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
Y, Cr, Cb = cv2.split(t_frame)
Yf_lap = cv2.filter2D(Y, -1, k_lap)
Yf_lap_e = cv2.filter2D(Y, -1, k_lap_e)
img_lap = cv2.cvtColor(cv2.merge((Yf_lap, Cr, Cb)), cv2.COLOR_YCrCb2BGR)
img_lap_e = cv2.cvtColor(cv2.merge((Yf_lap_e, Cr, Cb)), cv2.COLOR_YCrCb2BGR)
cframe = np.hstack((img, img_lap, img_lap_e))
cv2.imwrite('high.jpg', cframe)
