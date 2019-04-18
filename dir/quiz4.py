# 0612.py
import cv2
import numpy as np

src   = cv2.imread('../data/Lena.png', cv2.IMREAD_GRAYSCALE)
tmp_A   = cv2.imread('../data_tutorial/lenaEye.jpg', cv2.IMREAD_GRAYSCALE)
dst  = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)  # 출력 표시 영상

#
R1 = cv2.matchTemplate(src, tmp_A, cv2.TM_SQDIFF_NORMED)
minVal, _, minLoc, _ = cv2.minMaxLoc(R1)
print('TM_SQDIFF_NORMED:', minVal, minLoc)

w, h = tmp_A.shape[:2]
cv2.rectangle(dst, (200, 300), (minLoc[0]+h-120, minLoc[1]+w+120), (255, 0, 0), 2)

cv2.imshow('src', src)
cv2.imshow('dst',  dst)
cv2.waitKey()
cv2.destroyAllWindows()
