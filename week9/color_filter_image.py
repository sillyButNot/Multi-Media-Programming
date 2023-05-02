import cv2
import numpy as np

# ksize = int(input('Enter kernel size:'))
ksize = 3
kernel = np.ones((ksize, ksize), np.float32) / (ksize * ksize)
# ngain = float(input('Enter noise gain:'))
ngain = 80
# width = 320
# height = 240
width = 640
height = 480
# cap = cv2.VideoCapture(0, cv2.CAP_MSMF)
img = cv2.imread('image.jpg')
resize_frame = cv2.resize(img, (width, height))
t_frame = cv2.cvtColor(resize_frame, cv2.COLOR_BGR2YCrCb)
Y, Cr, Cb = cv2.split(t_frame)
noisy = np.clip(Y + np.random.random((height, width)) * ngain, 0, 255).astype(np.uint8)
filtered = cv2.filter2D(noisy, -1, kernel)
cnoisy = cv2.cvtColor(cv2.merge((noisy, Cr, Cb)), cv2.COLOR_YCrCb2BGR)
cfiltered = cv2.cvtColor(cv2.merge((filtered, Cr, Cb)), cv2.COLOR_YCrCb2BGR)
cframe = np.hstack((resize_frame, cnoisy, cfiltered))
cv2.imwrite('color_80.jpg', cframe)
