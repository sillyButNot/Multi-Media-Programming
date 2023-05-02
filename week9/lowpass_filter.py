import cv2
import numpy as np

ksize = int(input('Enter kernel size:'))
kernel = np.ones((ksize, ksize), np.float32) / (ksize * ksize)
ngain = float(input('Enter noise gain:'))

# width = 320
# height = 240
width = 640
height = 480
# cap = cv2.VideoCapture(0, cv2.CAP_MSMF)
cap = cv2.VideoCapture('video.mp4')
width = 640
height = 480
while True:
    ret, frame = cap.read()
    if ret:
        resize_frame = cv2.resize(frame, (width, height))
        img = cv2.cvtColor(resize_frame, cv2.COLOR_BGR2GRAY)
        noisy = np.clip(img + np.random.random((height, width)) * ngain, 0, 255).astype(np.uint8)
        filtered_img = cv2.filter2D(noisy, -1, kernel)
        cframe = np.hstack((img, noisy, filtered_img))
        cv2.imwrite('lowpass_3_5.jpg', cframe)
        cv2.imshow('Original, Noisy, Filtered', cframe)
        key = cv2.waitKey(33)
        if key == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
