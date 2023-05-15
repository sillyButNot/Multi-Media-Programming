import numpy as np
import time
import cv2


# 직접 접근
def gammaCorrect1(im, gamma):
    outImg = np.zeros(im.shape, im.dtype)
    rows, cols = im.shape
    for i in range(rows):
        for j in range(cols):
            outImg[i][j] = ((im[i][j] / 255.0) ** (1 / gamma)) * 255

    return outImg


# item을 이용한 접근
def gammaCorrect2(im, gamma):
    outImg = np.zeros(im.shape, im.dtype)
    rows, cols = im.shape

    for i in range(rows):
        for j in range(cols):
            gammaValue = ((im.item(i, j) / 255.0) ** (1 / gamma)) * 255
            outImg.itemset(i, j, gammaValue)
    return outImg


# 계산식 -> Look up table 대치+ item 접근
def gammaCorrect3(im, gamma):
    outImg = np.zeros(im.shape, im.dtype)
    rows, cols = im.shape
    LUT = []
    for i in range(256):
        LUT.append(((i / 255.0) ** (1 / gamma)) * 255)
    for i in range(rows):
        for j in range(cols):
            gammaValue = LUT[im.item(i, j)]
            outImg.itemset(i, j, gammaValue)
    return outImg


# look up table 대치 + numpy 어레이

def gammaCorrect3(im, gamma):
    outImg = np.zeros(im.shape, im.dtype)
    rows, cols = im.shape
    LUT = []
    for i in range(256):
        LUT.append(((i / 255.0) ** (1 / gamma)) * 255)
    for i in range(rows):
        for j in range(cols):
            gammaValue = LUT[im.item(i, j)]
            outImg.itemset(i, j, gammaValue)
    return outImg


def gammaCorrect4(im, gamma):
    outImg = np.zeros(im.shape, im.dtype)
    rows, cols = im.shape
    LUT = []
    for i in range(256):
        LUT.append(((i / 255.0) ** (1 / gamma)) * 255)

    LUT = np.array(LUT, dtype=np.uint8)
    outImg = LUT[im]
    return outImg


# img = cv2.imread(input("Enter image:"))
img = cv2.imread("IMG.jpg")
img = cv2.resize(img, (960, 1280))

print(img.shape)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gamma = 0.1
start_time = time.time()
gammaCorrect1(gray, gamma)
print("Eclipse time = %.4f" % (time.time() - start_time))
start_time = time.time()
gammaCorrect2(gray, gamma)
print("Eclipse time = %.4f" % (time.time() - start_time))
start_time = time.time()
gammaCorrect3(gray, gamma)
print("Eclipse time = %.4f" % (time.time() - start_time))
start_time = time.time()
gammaCorrect4(gray, gamma)
print("Eclipse time = %.4f" % (time.time() - start_time))
