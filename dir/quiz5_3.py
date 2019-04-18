import cv2

src = cv2.imread('../data/lena.jpg', cv2.IMREAD_GRAYSCALE)
rects = cv2.selectROI(src)

img = src[rects[1]:rects[1] + rects[3], rects[0]:rects[0]+rects[2]]

cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()
