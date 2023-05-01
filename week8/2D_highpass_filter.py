import cv2
import numpy as np

width = 320
height = 240
cap = cv2.VideoCapture(0, cv2.CAP_MSMF)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
k_lap = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
k_lap_e = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])

while True:
    ret, frame = cap.read()
    if ret:
        t_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)
        Y, Cr, Cb = cv2.split(t_frame)
        Yf_lap = cv2.filter2D(Y, -1, k_lap)
        Yf_lap_e = cv2.filter2D(Y, -1, k_lap_e)
        img_lap = cv2.cvtColor(cv2.merge((Yf_lap, Cr, Cb)), cv2.COLOR_YCrCb2BGR)
        img_lap_e = cv2.cvtColor(cv2.merge((Yf_lap_e, Cr, Cb)), cv2.COLOR_YCrCb2BGR)
        cframe = np.hstack((frame, img_lap, img_lap_e))
        cv2.imshow('High-pass filtered results', cframe)
        key = cv2.waitKey(33)
        if key == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
