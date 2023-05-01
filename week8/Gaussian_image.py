import cv2
import numpy as np

width = 640
height = 480
img = cv2.imread('s_.jpg')
height, width, channel = img.shape

resize_frame = cv2.resize(img, (width, height))
t_frame = cv2.cvtColor(resize_frame, cv2.COLOR_BGR2YCrCb)
Y, Cr, Cb = cv2.split(t_frame)
blur = cv2.GaussianBlur(Y, (0, 0), 2)
filtered_Y = np.clip(2.0 * Y - blur, 0, 255).astype(np.uint8)
cfiltered = cv2.cvtColor(cv2.merge((filtered_Y, Cr, Cb)), cv2.COLOR_YCrCb2BGR)
# cframe = np.hstack((cv2.flip(resize_frame, 1), cv2.flip(cfiltered, 1)))
cframe = np.hstack((resize_frame, cfiltered))
cv2.imwrite('gaussian.jpg', cframe)

