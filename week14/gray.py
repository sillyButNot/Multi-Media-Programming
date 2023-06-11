import cv2
import os
import glob
import random
import numpy as np


def rotate_resize_image(image_path, fname):
    # 이미지 읽기
    image = cv2.imread(image_path)
    height, width, channel = image.shape
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



    cv2.imwrite(fname, gray)

# 이미지 경로와 회전할 각도, 새로운 너비와 높이 지정
folder_path = "./image/"



count_img = 0
count_class = 5

list_file = 'list_'
fp = open(list_file, 'w')
# 이미지 회전 및 크기 조정 함수 호출
base_name = './image_qo/gray'
image_files = glob.glob(os.path.join(folder_path, "*.jpg"))

for image_file in image_files:
    fname = base_name + ('_%03d_%03d' % (count_img, count_class)) + '.jpg'
    rotate_resize_image(image_file, fname)
    count_img = count_img + 1
    print(fname)
    print('%s %d' % (fname, count_class), file=fp)


fp.close()