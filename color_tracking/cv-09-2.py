import numpy as np
import cv2

def tracking():
    try:
        print('카메라를 구동합니다.')
        cap = cv2.VideoCapture(0)
    except:
        print('카메라 구동 실패')
        return

    while True:
        ret, frame = cap.read()

        # BGR 을 HSV 모드로 전환
        # 캠에서 전송되는 비디오 프레임을 HSV 색공간으로 변경합니다.
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # HSV 에서 BGR 로 가정할 범위를 정의함
        lower_blue = np.array([110, 100, 100])
        upper_blue = np.array([130, 255, 255])

        lower_green = np.array([50, 100, 100])
        upper_green = np.array([70, 255, 255])

        lower_red = np.array([-10, 100, 100])
        upper_red = np.array([10, 255, 255])

        # HSV 이미지에서 청색만, 또는 초록색만 또는 빨간색만 추출하기 위한 임계값
        # lower_blue, upper_blue 로 지정한 범위에 있는지 체크한 후,
        # 범위에 해당하는 부분은 그 값 그대로, 나머지 부분은 0으로 채워서 반환
        mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
        mask_green = cv2.inRange(hsv, lower_green, upper_green)
        mask_red = cv2.inRange(hsv, lower_red, upper_red)

        # mask 와 원본 이미지를 비트 연산함
        res1 = cv2.bitwise_and(frame, frame, mask=mask_blue)
        res2 = cv2.bitwise_and(frame, frame, mask=mask_green)
        res3 = cv2.bitwise_and(frame, frame, mask=mask_red)

        cv2.imshow('BLUE', res1)
        cv2.imshow('GREEN', res2)
        cv2.imshow('RED', res3)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

    cv2.destroyAllWindows()

tracking()