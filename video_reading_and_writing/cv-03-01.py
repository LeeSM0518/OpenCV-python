import numpy as np
import cv2

def showVideo() :
    try :
        print('카메라를 구동합니다.')

        # 비디오 캡쳐를 위해 VideoCapture 객체 생성
        # 0 : 내장 카메라
        cap = cv2.VideoCapture(0)
    except :
        print('카메라 구동 실패')
        return

    cap.set(3, 480)
    cap.set(4, 320)

    while True :
        # 재생되는 비디오의 한 프레임씩 읽는다.
        # ret : 비디오 프레임 리딩 확인(True, False)
        # frame : 읽은 프레임
        ret, frame = cap.read()

        if not ret :
            print('비디오 읽기 오류')
            break

        # frame 을 흑백으로 변환
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 비디오 출력
        cv2.imshow('video', gray)

        k = cv2.waitKey(1)
        if k == 27 :
            break

    cap.release()
    cv2.destroyAllWindows()

showVideo()