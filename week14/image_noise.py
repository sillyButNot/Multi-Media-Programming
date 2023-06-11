import cv2
import os
import glob
import random
import numpy as np

# ksize = int(input('Enter kernel size:'))
ksize = 9
# rat_noise = float(input('Enter frequency of noise:'))
rat_noise =0.1

def rotate_resize_image(image_path, fname):
    # 이미지 읽기
    image = cv2.imread(image_path)
    height, width, channel = image.shape
    num_noise = int(width * height * rat_noise)

    t_frame = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
    Y, Cr, Cb = cv2.split(t_frame)
    for i in range(num_noise):
        y = random.randint(0, height - 1)
        x = random.randint(0, width - 1)
        Y[y][x] = 255
    filtered = cv2.medianBlur(Y, ksize)

    cfiltered = cv2.cvtColor(cv2.merge((filtered, Cr, Cb)), cv2.COLOR_YCrCb2BGR)

    cv2.imwrite(fname, cfiltered)

# 이미지 경로와 회전할 각도, 새로운 너비와 높이 지정
folder_path = "./image/"



count_img = 0
count_class = 5

list_file = 'list_'
fp = open(list_file, 'w')
# 이미지 회전 및 크기 조정 함수 호출
base_name = './image_qo/noise'
image_files = glob.glob(os.path.join(folder_path, "*.jpg"))

for image_file in image_files:
    fname = base_name + ('_%03d_%03d' % (count_img, count_class)) + '.jpg'
    rotate_resize_image(image_file, fname)
    count_img = count_img + 1
    print(fname)
    print('%s %d' % (fname, count_class), file=fp)


fp.close()