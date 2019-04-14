# 0202.py
import cv2

imageFile = '../data/lena.jpg'
img = cv2.imread(imageFile) # cv2.imread(imageFile, cv2.IMREAD_COLOR)

cv2.imshow('img', img)
