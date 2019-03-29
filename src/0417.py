# 0417.py
import cv2
import numpy as np

src1 = cv2.imread('../data/lena.jpg', cv2.IMREAD_GRAYSCALE)
src2 = np.zeros(shape=(512,512), dtype=np.uint8) + 100
src3 = cv2.imread('../data/lena.jpg')

dst1 = src1 + src2
dst2 = cv2.subtract(src1, src2)
dst3 = cv2.add(src1, src2)
# dst2 = cv2.add(src1, src2, dtype = cv2.CV_8U)

cv2.imshow('dst1',  dst1)
cv2.imshow('dst2',  dst2)
cv2.imshow('dst3',  dst3)
cv2.imshow('original', src3)
cv2.waitKey()    
cv2.destroyAllWindows()
