# 0406.py
import cv2
import numpy as np

#src = cv2.imread('./data/lena.jpg', cv2.IMREAD_GRAYSCALE)
src = cv2.imread('../data/lena.jpg')
roi = cv2.selectROI(src)
print('roi = ', roi)
dst = src 
#dst = np.zeros(src.shape, dtype=src.dtype)
N = 64 # 8, 32, 64
#height, width = src.shape    # 그레이스케일 영상
height, width, _ = src.shape # 컬러영상

h = height // N
w = width  // N
for i in range(int(roi[1]//10), int(roi[3]//10)):
    for j in range(int(roi[0])//10, int(roi[2]//10)):
        y = i*h
        x = j*w       
        roi = src[y:y+h, x:x+w]        
#        dst[y:y+h, x:x+w] = cv2.mean(roi)[0]   # 그레이스케일 영상
        dst[y:y+h, x:x+w] = cv2.mean(roi)[0:3] # 컬러영상


cv2.imshow('dst', dst)

cv2.waitKey()
cv2.destroyAllWindows()
 
