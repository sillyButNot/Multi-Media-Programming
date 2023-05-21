import cv2
import numpy as np

# img = cv2.imread(input("Enter image file:"))
img = cv2.imread('sky.jpg')
# Thres = int(input("Enter accumulation threshold:"))
Thres = int(130)
minLineLength = 5
maxLineGap = 1

h = 320
w = 240
rimg = cv2.resize(img, (h, w))
img2 = rimg.copy()

Y, Cr, Cb = cv2.split(cv2.cvtColor(rimg, cv2.COLOR_BGR2YCrCb))
edges = cv2.Canny(Y, 100, 200)
edge_color = cv2.cvtColor(cv2.merge((edges, Cr, Cb)), cv2.COLOR_YCrCb2BGR)  # 잘 안보이면 edges, edges, edges

lines = cv2.HoughLinesP(edges, 1, np.pi / 180, Thres, None, minLineLength, maxLineGap)
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img2, (x1, y1), (x2, y2), (0, 255, 0), 2)

merged = np.hstack((rimg, edge_color, img2))
cv2.imwrite('hough_p.jpg', merged)


