import cv2
import numpy as np


def Build_H(N, f_radius):
    HN = N / 2
    H = np.zeros((N, N), dtype=np.float32)
    for y in range(N):
        for x in range(N):
            fy = (y - HN) / HN
            fx = (x - HN) / HN
            radius = np.sqrt(fy * fy + fx * fx)
            if radius <= f_radius:
                H[y][x] = 1
    return H

def Filter2D_FT(Fin, H):
    mag = np.abs(Fin)
    phs = np.angle(Fin)
    fmag = H * mag
    return fmag * np.exp(1j * phs)

N = 256
# fcut = float(input("Enter cut-off radius:[0~1]"))
fcut = 0.9

H = Build_H(N, fcut)
img_H = (H * 255).astype(np.uint8)
img = cv2.imread('image/hand1.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) / 255
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
r_gray = cv2.resize(gray, (N, N))
# cv2.imwrite('image/hand_22.jpg', r_gray)
F = np.fft.fft2(r_gray)
F_sh = np.fft.fftshift(F)
FF = Filter2D_FT(F_sh, H)
iF_sh = np.fft.ifftshift(FF)
i_gray = np.clip(np.abs(np.fft.ifft2(iF_sh)), 0, 255)
cframe = np.hstack((img_H, r_gray, i_gray))
cv2.imwrite('image/hand_0.9.jpg', cframe)
