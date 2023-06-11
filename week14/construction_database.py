import cv2
import numpy as np
import time

# base_name = input('Enter base file name:')
base_name = './images/tr_image'
# delay = float(input('Enter capture delay (in sec):'))
delay = float(0.1)

# num_class = int(input('Enter number of classes:'))
num_class = int(5)
# num_files = int(input('Enter number of images pre class:'))
num_files = int(10)
# list_file = input('Enter list file name:')
list_file = 'list_tr'
# cap = cv2.VideoCapture(0, cv2.CAP_MSMF)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
fp = open(list_file, 'w')
write = True
print("Press w to start..")
count_img = count_class = 0

while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow("captured", frame)
        if write:
            fname = base_name + ('_%03d_%03d' % (count_img, count_class)) + '.jpg'
            cv2.imwrite(fname, frame)
            print(fname)
            print('%s %d' % (fname, count_class), file=fp)
            count_img += 1
    if count_img == num_files:
        count_img = 0
        count_class += 1
        if count_class == num_class:
            break
        write = False
        print('Press w to restart')

    key = cv2.waitKey(33)
    if key == ord('w'):
        write = True
    time.sleep(delay)

fp.close()
cap.release()
cv2.destroyAllWindows()
