import cv2
import numpy as np

ksize = int(input('Enter kernel size:'))
kernel = np.ones((ksize, ksize), np.float32) / (ksize * ksize)
# cap = cv2.VideoCapture(0, cv2.CAP_MSMF)
cap = cv2.VideoCapture('video.mp4')
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
width = 640
height = 480
while True:
    ret, frame = cap.read()
    if ret:
        resize_frame = cv2.resize(frame, (width, height))
        filtered_frame = cv2.filter2D(resize_frame, -1, kernel)
        cframe = np.hstack((resize_frame, filtered_frame))
        cv2.imshow('Image', cframe)
        key = cv2.waitKey(33)
        if key == ord('q'):
            break
    else:
        cap = cv2.VideoCapture('video.mp4')
cap.release()
cv2.destroyAllWindows()
