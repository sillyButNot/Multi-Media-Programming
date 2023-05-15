import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 30)
while True:
    ret, img = cap.read()
    if ret:
        t_frame = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
        Y, Cr, Cb = cv2.split(t_frame)
        Y_ = cv2.equalizeHist(Y)
        merged = cv2.cvtColor(cv2.merge((Y_, Cr, Cb)), cv2.COLOR_YCrCb2BGR)

        cimg = np.hstack((img, merged))
        cv2.imshow('Histogram stretching', cimg)
        key = cv2.waitKey(33)
        if key == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
