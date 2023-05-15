import cv2
import numpy as np

W = 640
H = 480
# bimg = cv2.imread(input("Enter background image:"))
bimg = cv2.imread("read.jpg")
bimg = cv2.resize(bimg, (W, H))
bb, bg, br = cv2.split(bimg)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, W)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, H)

while True:
    ret, img = cap.read()
    if ret:
        b, g, r = cv2.split(img)
        for y in range(H):
            for x in range(W):
                if g.item(y, x) > 120 and b.item(y, x) > 120 and r.item(y, x) > 120:
                    b.itemset(y, x, bb.item(y, x))
                    g.itemset(y, x, bg.item(y, x))
                    r.itemset(y, x, br.item(y, x))
        timg = cv2.merge((b, g, r))
        cimg = np.hstack((bimg, timg))
        cv2.imshow('Chroma key', cimg)
        key = cv2.waitKey(33)
        if key == ord('q'):
            break
    else:
        print("hi")
cap.release()
cv2.destroyAllWindows()
