import cv2

# cv2.VideoCapture(n)
# 내장 카메라나 외장 카메라를 받아온다. n은 카메라의 장치 번호이다.
# 0은 내장 카메라
capture = cv2.VideoCapture(0)

# capture.set(option, n)
# 카메라의 속성을 설정할 수 있다.
# option : 프레임의 너비와 높이
# n : 값
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    # capture.read() : 카메라의 상태 및 프레임을 받아온다.
    # ret : 카메라가 정상 작동시 True, 작동하지 않으면 False
    # frame : 현재 프레임 저장
    ret, frame = capture.read()

    # cv2.imshow('원도우 창 제목', 이미지)
    cv2.imshow("VideoFrame", frame)

    # cv2.waitkey(time) : time 마다 키 입력상태를 받아온다.
    if cv2.waitKey(1) > 0: break

# 메모리 해제(카메라 해제)
capture.release()
# 모든 윈도우창 닫기
cv2.destroyAllWindows()