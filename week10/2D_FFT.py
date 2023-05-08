import cv2
import numpy as np

cap = cv2.VideoCapture('image/video.mp4')

# cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width, height)

while True:
    ret, img = cap.read()
    if ret:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        F = np.fft.fft2(gray)
        Fshift = np.fft.fftshift(F)
        mag_spc = np.clip((20 * np.log(np.abs(Fshift))), 0, 255).astype(np.uint8)
        gray_re = cv2.resize(gray, (640, 320))
        mag_spc = cv2.resize(mag_spc, (640, 320))

        cframe = np.hstack((gray_re, mag_spc))
        cv2.imshow('2D-FFT', cframe)
        key = cv2.waitKey(33)
        if key == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
