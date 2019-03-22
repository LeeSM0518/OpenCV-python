import numpy as np
import cv2
# 무작위 색상 값을 추출하기 위함
from random import shuffle

# BGR 색상값을 사용하기 위해 0~255 값을 가진 리스트 생성
b = [i for i in range(256)]
g = [i for i in range(256)]
r = [i for i in range(256)]

# 마우스 이벤트를 처리할 콜백 함수
def onMouse(event, x, y, flags, param):
    # event : 마우스 이벤트
    # x, y : 마우스 이벤트가 일어난 위치
    # flags 플래그
    # param : cv2.setMouseCallback() 함수
    if event == cv2.EVENT_LBUTTONDOWN:
        shuffle(b), shuffle(g), shuffle(r)
        cv2.circle(param, (x, y), 50, (b[0], g[0], r[0]), -1)

def mouseBrush():
    img = np.zeros((512, 512, 3), np.uint8)
    cv2.namedWindow('paint')
    cv2.setMouseCallback('paint', onMouse, param=img)

    while True:
        cv2.imshow('paint', img)
        k = cv2.waitKey(1)

        if k == 27:
            break

    cv2.destroyAllWindows()

mouseBrush()