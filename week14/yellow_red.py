import cv2

import os
import glob

def adjust_color(image_path, factor, fname):
    # 이미지 로드
    image = cv2.imread(image_path)

    # 이미지를 YCrCb 색 공간으로 변환
    image_ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

    # YCrCb 채널 분리
    y, cr, cb = cv2.split(image_ycrcb)

    # YCrCb 채널 조정
    cr_adjusted = cv2.add(cr, factor)  # Cr 채널을 노랗게 만듦
    # cr_adjusted = cv2.subtract(cr, factor)  # Cr 채널을 빨갛게 만듦

    # YCrCb 채널 병합
    image_ycrcb_adjusted = cv2.merge([y, cr_adjusted, cb])

    # YCrCb 색 공간을 BGR 색 공간으로 변환
    image_bgr_adjusted = cv2.cvtColor(image_ycrcb_adjusted, cv2.COLOR_YCrCb2BGR)

    # 조정된 이미지 출력

    cv2.imwrite(fname, image_bgr_adjusted)

# 채널 조정 팩터 (-255 ~ 255 사이의 값을 사용)


# 이미지 색 조정 함수 호출



folder_path = "./image/"
# 양수 값은 노랗게, 음수 값은 빨갛게 조정
factor = -10

count_img = 0
count_class = 5

list_file = 'list_'
fp = open(list_file, 'w')
# 이미지 회전 및 크기 조정 함수 호출
base_name = './image_qo/red5'
image_files = glob.glob(os.path.join(folder_path, "*.jpg"))

for image_file in image_files:
    fname = base_name + ('_%03d_%03d' % (count_img, count_class)) + '.jpg'
    adjust_color(image_file, factor, fname)
    count_img = count_img + 1
    print(fname)
    print('%s %d' % (fname, count_class), file=fp)
