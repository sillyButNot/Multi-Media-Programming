import cv2

import os
import glob
def flip_image(image_path, fname):
    # 이미지 로드
    image = cv2.imread(image_path)

    # 이미지 좌우 반전
    flipped_image = cv2.flip(image, 1)

    # 반전된 이미지 저장

    cv2.imwrite(fname, flipped_image)

    # 반전된 이미지 출력




folder_path = "./image/"



count_img = 0
count_class = 5

list_file = 'list_'
fp = open(list_file, 'w')
# 이미지 회전 및 크기 조정 함수 호출
base_name = './image_qo/flip'
image_files = glob.glob(os.path.join(folder_path, "*.jpg"))

for image_file in image_files:
    fname = base_name + ('_%03d_%03d' % (count_img, count_class)) + '.jpg'
    flip_image(image_file, fname)
    count_img = count_img + 1
    print(fname)
    print('%s %d' % (fname, count_class), file=fp)

