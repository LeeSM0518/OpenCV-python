import numpy as np
import cv2

def hsv():
    # Blue 픽셀 1개에 해당하는 numpy array 를 생성한다. Green, Red 도 동일
    blue = np.uint8([[[255, 0, 0]]])
    green = np.uint8([[[0, 255, 0]]])
    red = np.uint8([[[0, 0, 255]]])

    hsb_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
    hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
    hsv_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
    
    print('HSV for BLUE: ', hsb_blue)
    print('HSV for GREEN: ', hsv_green)
    print('HSV for RED: ', hsv_red)

hsv()