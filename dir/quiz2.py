# 0404.py
import cv2
##import numpy as np

# 이미지 불러옴
img = cv2.imread('../data/lena.jpg') # cv2.IMREAD_COLOR
# 바꿔질 이미지 저장
img_change = cv2.imread('../data/lena.jpg')
# 이미지에 검은색으로 채워진 원을 그림
img = cv2.circle(img, (270, 286), 100, (0, 0, 0), -1)

print(img.shape)

for i in range(512) :
    for j in range(512) :
        # 검은 원을 그린 원의 좌표를 찍어 0인지 판변
        # 0 false, 1 true
        if img[i][j].any() != 0 :
            # 검은색으로 그려준다
            img_change[i][j] = 0

cv2.imshow('img2', img)
cv2.imshow('img', img_change)
cv2.waitKey()
cv2.destroyAllWindows()
