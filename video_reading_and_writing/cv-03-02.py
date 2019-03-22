import numpy as np
import cv2

def writeVideo():
    try :
        print('카메라 구동.')
        cap = cv2.VideoCapture(0)
    except:
        print('카메라 구동 실패')
        return

    # 초당 프레임
    fps = 20.0

    # 카메라 가로, 세로 지정
    width = int(cap.get(3))
    height = int(cap.get(4))

    # DIVX 코덱을 적용
    fcc = cv2.VideoWriter_fourcc('D','I','V','X')

    # 비디오 저장을 위한 객체 생성
    out = cv2.VideoWriter('mycam.avi', fcc, fps, (width, height))
    print('녹화를 시작합니다.')

    while True :
        ret, frame = cap.read()

        if not ret:
            print('비디오 읽기 오류')
            break

        # 비디오 출력
        cv2.imshow('video', frame)
        # 프레임 저장
        out.write(frame)

        k = cv2.waitKey(1)
        if k == 27:
            print('녹화를 종료합니다')
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

writeVideo()