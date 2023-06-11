import cv2
import numpy as np
import random

# ksize = int(input('Enter kernel size:'))
ksize = 9
# rat_noise = float(input('Enter frequency of noise:'))
rat_noise =0.1

img = cv2.imread('./images/tr_image_000_000.jpg')
height, width, channel = img.shape
num_noise = int(width * height * rat_noise)

t_frame = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
Y, Cr, Cb = cv2.split(t_frame)
for i in range(num_noise):
    y = random.randint(0, height - 1)
    x = random.randint(0, width - 1)
    Y[y][x] = 255

filtered = cv2.medianBlur(Y, ksize)
cnoisy = cv2.cvtColor(cv2.merge((Y, Cr, Cb)), cv2.COLOR_YCrCb2BGR)
cfiltered = cv2.cvtColor(cv2.merge((filtered, Cr, Cb)), cv2.COLOR_YCrCb2BGR)
cframe = np.hstack((img, cnoisy, cfiltered))
cv2.imwrite('median.jpg', cframe)