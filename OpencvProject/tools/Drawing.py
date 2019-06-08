# 1111.py
import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import subprocess

class CharacterRecognition:
    # 크기가 512, 512 이고 int8 형
    dst = np.zeros(shape=(512, 512, 3), dtype=np.uint8)
    src = cv2.imread("../doc/source/images/blackboard.JPG")
    blackBoard = cv2.imread("../doc/source/images/blackboard.JPG")
    fontpath = "../doc/source/fonts/NanumPen.ttf"
    font = ImageFont.truetype(fontpath, 50)
    img_pil = Image.fromarray(dst)
    draw = ImageDraw.Draw(img_pil)

    width = height = 50

    # 이미지의 가장 바깥쪽의 contour 만 추출
    mode = cv2.RETR_LIST
    method = cv2.CHAIN_APPROX_NONE

    x_img = np.zeros(shape=(28, 28), dtype=np.uint8)

    leftEdge = 99999
    rightEdge = -1
    upEdge = 99999
    downEdge = -1

    radius = 10

    @classmethod
    def resetEdge(cls):
        cls.leftEdge = 99999
        cls.rightEdge = -1
        cls.upEdge = 99999
        cls.downEdge = -1

    @classmethod
    def onMouse(cls, event, x, y, flags, param):

        if event == cv2.EVENT_MOUSEMOVE:
            if flags & cv2.EVENT_FLAG_LBUTTON:
                cv2.circle(cls.dst, (x, y), cls.radius, (255, 255, 255), -1)

                if cls.leftEdge > x:
                    cls.leftEdge = x
                elif cls.rightEdge < x:
                    cls.rightEdge = x

                if cls.upEdge > y:
                    cls.upEdge = y
                elif cls.downEdge < y:
                    cls.downEdge = y

        cv2.imshow('dst', cls.dst)

    @classmethod
    def viewWindow(cls):
        cv2.imshow('blackboard', cls.blackBoard)
        cv2.imshow('dst', cls.dst)
        cv2.setMouseCallback('dst', cls.onMouse)

    @classmethod
    def fileRead(cls, fileName):
        defaultInputFront = 'python ./classify-hangul.py ../doc/source/images/'
        defaultInputBack = ' --label-file ../labels/2350-common-hangul.txt'
        defaultInput = defaultInputFront + fileName + defaultInputBack
        result = subprocess.check_output(defaultInput, shell=True)
        splitResult = result.split()
        letter = splitResult[3].decode('utf-8')

        return letter

    @classmethod
    def mainMethod(cls):
        cls.viewWindow()
        while True:
            key = cv2.waitKey(25)

            if key == 27:
                break

            elif key == ord(' '):
                cls.width += 30

            elif key == ord('\b'):
                for i in range(cls.height, cls.height + 50):
                    for j in range(cls.width - 30, cls.width + 5):
                        cls.blackBoard[i][j] = cls.src[i][j]
                cv2.imshow('blackboard', cls.blackBoard)

                cls.width -= 30

            elif key == ord('s'):
                cls.height += 50
                cls.width = 50

            elif key == ord('q'):
                cls.blackBoard = cls.src

                cls.dst[:, :] = 0
                cv2.imshow('dst', cls.dst)

            elif key == 13:
                resized = cv2.resize(cls.dst, dsize=(64, 64), interpolation=cv2.INTER_AREA)
                cv2.imwrite('../doc/source/images/resized.jpg', resized)
                img_pil = Image.fromarray(cls.blackBoard)
                draw = ImageDraw.Draw(img_pil)
                draw.text((cls.width, cls.height), cls.fileRead('resized.jpg'), font=cls.font, fill=(255, 255, 255, 0))
                cls.blackBoard = np.array(img_pil)
                cv2.imshow('blackboard', cls.blackBoard)
                cls.width += 30
                cls.resetEdge()
                cls.dst[:, :] = 0
                cv2.imshow('dst', cls.dst)

        cv2.destroyAllWindows()


CharacterRecognition.mainMethod()