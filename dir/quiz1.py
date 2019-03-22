# 0310.py
import numpy as np
import cv2

width, height = 512, 512
x, y, R = 256, 256, 50
direction = 0  # right

while True:
    key = cv2.waitKeyEx(30)
    if key == 0x1B:
        break

    # 방향키 방향전환
    elif key == 0x61:  # righta
        direction = 0
    elif key == 0x62:  # down
        direction = 1
    elif key == 0x63:  # left
        direction = 2
    elif key == 0x64:  # up
        direction = 3

    # 방향으로 이동
    if direction == 0:  # right
        x += 10
    elif direction == 1:  # down
        y += 10
    elif direction == 2:  # left
        x -= 10
    else:  # 3, up
        y -= 10

    #   경계확인
    if x < R - 100:
        x = width + 50
        direction = 2
    if x > width - R + 100:
        x = -50
        direction = 0
    if y < R - 100:
        y = height + 50
        direction = 3
    if y > height - R + 100:
        y = -50
        direction = 1

    # 지우고, 그리기
    img = np.zeros((width, height, 3), np.uint8) + 255  # 지우기
    cv2.circle(img, (x, y), R, (0, 0, 255), -1)
    cv2.imshow('img', img)

cv2.destroyAllWindows()