import numpy as np
import cv2

def showImage() :
    imgfile = '../data/image.png'

    # imread : 이미지 파일을 읽기 위한 객체 리턴
    # 매개변수 : (이미지 파일 경로, 이미지 파일을 읽는 방식)
    img = cv2.imread(imgfile, cv2.IMREAD_COLOR)

    # 이미지 크기를 변경시킬 수 있는 창을 만듬
    # 윈도우 사이즈 플래그
    # cv2.WINDOW_AUTOSIZE : 원본 이미지 크기로 고정하여 윈도우 생성
    # cv2.WINDOW_NORMAL : 원본 이미지 크기로 윈도우를 생성, 사용자가 크기를 조절할 수 있음
    cv2.namedWindow('jeny', cv2.WINDOW_NORMAL)

    # imshow : 이미지 객체 img를 화면에 나타내기 위한 함수
    cv2.imshow('jeny', img)

    # waitKey : 지정된 시간동안 키보드 입력을 기다리는 함수
    k = cv2.waitKey(0)

    # ESC 키를 누르면 그냥 프로그램 종료
    if k == 27 :
        # 생성한 모든 윈도우를 제거한다.
        cv2.destroyAllWindows()
    # c 키를 누르면 파일 복사
    elif k == ord('c') :
        cv2.imwrite('./jeny_copy.jpg', img)

showImage()