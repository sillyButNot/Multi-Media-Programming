import cv2
import numpy as np

N = 256
img = cv2.imread('image/dot.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
r_gray = cv2.resize(gray, (N, N))
F = np.fft.rfft2(r_gray)
F_sh = np.fft.fftshift(F)
iF_sh = np.fft.ifftshift(F_sh)
i_gray = np.clip(np.abs(np.fft.irfft2(iF_sh)), 0, 255)
cframe = np.hstack((r_gray, i_gray))

cv2.imwrite('image/dot_.jpg', cframe)
