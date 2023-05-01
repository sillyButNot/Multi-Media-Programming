import cv2
import numpy as np

ksize = int(input('Enter kernel size:'))
kernel = np.ones((ksize, ksize), np.float32) / (ksize * ksize)
# cap = cv2.VideoCapture(0, cv2.CAP_MSMF)
# cap = cv2.VideoCapture('video.mp4')
img = cv2.imread('s.jpg')
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
width = 640
height = 480
resize_frame = cv2.resize(img, (width, height))
filtered_frame = cv2.filter2D(img, -1, kernel)
cv2.imwrite('filterd_9.jpg', filtered_frame)


