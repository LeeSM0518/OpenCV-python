# 0404.py
import cv2
##import numpy as np

img = cv2.imread('../data/lena.jpg') # cv2.IMREAD_COLOR
img_change = cv2.imread('../data/lena.jpg')
img = cv2.circle(img, (270, 286), 100, (0, 0, 0), -1)

print(img.shape)

for i in range(512) :
    for j in range(512) :
        if img[i][j].any() != 0 :
            img_change[i][j] = 0

cv2.imshow('img2', img)
cv2.imshow('img', img_change)
cv2.waitKey()
cv2.destroyAllWindows()
