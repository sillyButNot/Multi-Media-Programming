import cv2
import numpy as np

# ksize = int(input('Enter kernel size:'))
ksize = 11
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
noisy_22 = np.clip(Y + np.random.random((height, width)) * 22, 0, 100).astype(np.uint8)
noisy_45 = np.clip(Y + np.random.random((height, width)) * 45, 0, 100).astype(np.uint8)
noisy_80 = np.clip(Y + np.random.random((height, width)) * 80, 0, 100).astype(np.uint8)
filtered_22 = cv2.filter2D(noisy_22, -1, kernel)
filtered_45 = cv2.filter2D(noisy_45, -1, kernel)
filtered_80 = cv2.filter2D(noisy_80, -1, kernel)
cfiltered_22 = cv2.cvtColor(cv2.merge((filtered_22, Cr, Cb)), cv2.COLOR_YCrCb2BGR)
cfiltered_45 = cv2.cvtColor(cv2.merge((filtered_45, Cr, Cb)), cv2.COLOR_YCrCb2BGR)
cfiltered_80 = cv2.cvtColor(cv2.merge((filtered_80, Cr, Cb)), cv2.COLOR_YCrCb2BGR)

cframe = np.hstack((cfiltered_22, cfiltered_45,cfiltered_80))
cv2.imwrite('color_.jpg', cframe)
