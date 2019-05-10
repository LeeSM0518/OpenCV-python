# 0803.py
import cv2
import numpy as np

#1
src = cv2.imread('../data/numberplate6.jpg')
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
eigen = cv2.cornerMinEigenVal(gray, blockSize=5)
print('eigen.shape=', eigen.shape)

#2
i = 0.0
while True:
    i += 0.01
    T = 0.01 + i
    corners  = np.argwhere(eigen > T)
    print(corners)
    corners[:,[0, 1]] = corners[:,[1, 0]] # switch x, y
    print('len(corners ) =', len(corners ))
    if len(corners) < 300 :
        break

dst = src.copy()
for x, y in corners :    
    cv2.circle(dst, (x, y), 4, (0,0,255), 2)
    
cv2.imshow('dst',  dst)
cv2.waitKey()
cv2.destroyAllWindows()
