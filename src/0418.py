# 0418.py: OpenCV-Python Tutorials 참조
import cv2
import numpy as np
src1 = cv2.imread('../data/lena.jpg')
src2 = cv2.imread('../data/opencv_logo.png')
cv2.imshow('src2',  src2)

# rows, cols, channels = src2.shape
# M2 = cv2.getRotationMatrix2D( (rows/2, cols/2), -45, 1.0 )
# dst2 = cv2.warpAffine( src2, M2, (rows, cols))

#1 : src2의 전체 크기에 대한 src1의 영역을 roi에 저장한다.
rows,cols,channels = src2.shape
roi = src1[0:rows, 0:cols]

#2 : 컬러영상 src2를 그레이스케일 영상 gray로 변환
gray = cv2.cvtColor(src2,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)
# 전경과 배경을 분활하기 위해 이진 영상 mask를 생성하고
ret, mask = cv2.threshold(gray, 160, 255, cv2.THRESH_BINARY)
# 비트 반전 영상을 생성한다.
mask_inv = cv2.bitwise_not(mask)    # 반전
cv2.imshow('mask',  mask)
cv2.imshow('mask_inv',  mask_inv)

#3 : roid 영상에서 mask의 255(흰색 영역)인 화소에서만 bitwise_and() 함수로
# src1의 배경영역을 복사하고, 전경 영역은 0(검은색)인 그림에 src1_bg를 생성한다.
src1_bg = cv2.bitwise_and(roi, roi, mask = mask)
cv2.imshow('src1_bg',  src1_bg)

#4 : mask_inv 마스크를 사용하여 src2에서 전경 영역을 src2_fg에 복사한다.
src2_fg = cv2.bitwise_and(src2, src2, mask = mask_inv)
cv2.imshow('src2_fg',  src2_fg)

#5 : cv2.bitwise_or()로 src1_bg와 src2_fg 를 비트 OR 연산하여 dst를 생성한다.
##dst = cv2.add(src1_bg, src2_fg)
dst = cv2.bitwise_or(src1_bg, src2_fg)
cv2.imshow('dst',  dst)

#6 : dst를 레나 그림에 붙여넣는다.
src1[0:rows, 0:cols] = dst

cv2.imshow('result',src1)
cv2.waitKey(0)
cv2.destroyAllWindows()
