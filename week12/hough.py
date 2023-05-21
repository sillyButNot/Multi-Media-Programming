import cv2
import numpy as np

# img = cv2.imread(input("Enter image file:"))
img = cv2.imread('green.jpg')
# Thres = int(input("Enter accumulation threshold:"))
Thres = int(120)

h = 320
w = 240
rimg = cv2.resize(img, (h, w))
img2 = rimg.copy()

rimg = cv2.GaussianBlur(rimg, (3, 3), 0)
Y, Cr, Cb = cv2.split(cv2.cvtColor(rimg, cv2.COLOR_BGR2YCrCb))
edges = cv2.Canny(Y, 100, 200)
edge_color = cv2.cvtColor(cv2.merge((edges, Cr, Cb)), cv2.COLOR_YCrCb2BGR)  # 잘 안보이면 edges, edges, edges

lines = cv2.HoughLines(edges, 1, np.pi / 180, Thres)
for line in lines:
    r, theta = line[0]
    tx, ty = np.cos(theta), np.sin(theta)
    x0, y0 = tx * r, ty * r
    x1, y1 = int(x0 + w * (-ty)), int(y0 + h * tx)
    x2, y2 = int(x0 - w * (-ty)), int(y0 - h * tx)
    cv2.line(img2, (x1, y1), (x2, y2), (255, 0, 0), 2)

merged = np.hstack((rimg, edge_color, img2))
cv2.imwrite('hough.jpg', merged)
# cv2.waitKey()
# cv2.destroyAllWindows()
