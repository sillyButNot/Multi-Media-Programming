import cv2
import os
import glob

def rotate_resize_image(image_path, new_width, new_height, fname):
    # 이미지 읽기
    image = cv2.imread(image_path)

    # 이미지 회전
    rows, cols, _ = image.shape
    rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

    # 이미지 크기 조정
    resized_image = cv2.resize(rotated_image, (new_width, new_height))

    # 크기 조정된 이미지 저장
    cv2.imwrite("resized_image.jpg", resized_image)

    # 크기 조정된 이미지 보여주기

    cv2.imwrite(fname, resized_image)

# 이미지 경로와 회전할 각도, 새로운 너비와 높이 지정
folder_path = "./image/"

new_width = 1008
new_height = 567
count_img = 0
count_class = 5

list_file = 'list_'
fp = open(list_file, 'w')
# 이미지 회전 및 크기 조정 함수 호출
base_name = './image_qo/tr_image'
image_files = glob.glob(os.path.join(folder_path, "*.jpg"))

for image_file in image_files:
    fname = base_name + ('_%03d_%03d' % (count_img, count_class)) + '.jpg'
    rotate_resize_image(image_file, new_width, new_height, fname)
    count_img = count_img + 1
    print(fname)
    print('%s %d' % (fname, count_class), file=fp)


fp.close()