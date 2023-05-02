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
img = cv2.cvtColor(resize_frame, cv2.COLOR_BGR2GRAY)
noisy = np.clip(img + np.random.random((height, width)) * ngain, 0, 255).astype(np.uint8)
filtered_img = cv2.filter2D(noisy, -1, kernel)
cframe = np.hstack((img, noisy, filtered_img))
cv2.imwrite('filter_noise_80.jpg', filtered_img)

