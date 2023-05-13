import cv2
import numpy as np

img = cv2.imread('image/dog.jpg')
# print(img.shape)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
F = np.fft.fft2(gray)
Fshift = np.fft.fftshift(F)
mag_spc = np.clip((20 * np.log(np.abs(Fshift))), 0, 255).astype(np.uint8)
# mag_spc1 = np.clip((40 * np.log(np.abs(Fshift))), 0, 255).astype(np.uint8)

cframe = np.hstack((gray, mag_spc))

cv2.imwrite('image/dog_.jpg', cframe)

