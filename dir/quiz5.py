import cv2
import numpy as np

def func():
    src = cv2.imread('../data/lena.jpg', cv2.IMREAD_GRAYSCALE)
    rects = cv2.selectROI(src)

    N = 32

    h= (rects[3]) // N
    w = (rects[2]) // N

    for i in range(N):
        for j in range(N):
            y = i * h + rects[1]
            x = j * w + rects[0]
            roi = src[y:y + h, x: x + w]
            src[y:y + h, x:x + w] = cv2.mean(roi)[0]

    cv2.imshow('dst', src)
    cv2.waitKey()
    cv2.destroyAllWindows()


while True:
    func()