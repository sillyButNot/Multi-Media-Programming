import cv2
import numpy as np

W = 640
H = 480
# bimg = cv2.imread(input("Enter background image:"))
bimg = cv2.imread('background.jpg')
bimg = cv2.resize(bimg, (W, H))
bb, bg, br = cv2.split(bimg)

img = cv2.imread('green.jpg')
img = cv2.resize(img, (W, H))
b, g, r = cv2.split(img)

for y in range(H):
    for x in range(W):
        if g.item(y, x) > 20 and b.item(y, x) < 30 and r.item(y, x) < 30:
            b.itemset(y, x, bb.item(y, x))
            g.itemset(y, x, bg.item(y, x))
            r.itemset(y, x, br.item(y, x))
timg = cv2.merge((b, g, r))
# cimg = np.hstack((bimg, timg))
cv2.imwrite('duck_r.jpg', timg)

