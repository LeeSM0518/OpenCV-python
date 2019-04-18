import numpy as np
import cv2

def tracking():
    img = cv2.imread('../data/news.png')
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # HSV 에서 BGR 로 가정할 범위를 정의함
    lower_blue = np.array([0, 60, 80])
    upper_blue = np.array([12, 255, 255])

    # HSV 이미지에서 청색만, 또는 초록색만 또는 빨간색만 추출하기 위한 임계값
    # lower_blue, upper_blue 로 지정한 범위에 있는지 체크한 후,
    # 범위에 해당하는 부분은 그 값 그대로, 나머지 부분은 0으로 채워서 반환
    mask_blue = cv2.inRange(img_hsv, lower_blue, upper_blue)

    # mask 와 원본 이미지를 비트 연산함
    res1 = cv2.bitwise_and(img, img, mask=mask_blue)

    cv2.imshow('img',img)
    cv2.imshow('BLUE', res1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

tracking()
