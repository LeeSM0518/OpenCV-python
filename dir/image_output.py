import cv2

# 경로, mode 로 이미지를 불러옴
image = cv2.imread('../data/image.png', cv2.IMREAD_UNCHANGED)

cv2.imshow('jeny', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

image = cv2.imread("../data/image.png", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

canny = cv2.Canny(image, 100, 255)
sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 3)
laplacian = cv2.Laplacian(gray, cv2.CV_8U, ksize=3)

cv2.imshow("canny", canny)
cv2.imshow("sobel", sobel)
cv2.imshow("laplacian", laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()