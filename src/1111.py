# 1111.py
import cv2
import numpy as np


class CharacterRecognition:

    ann = cv2.ml_ANN_MLP.load('../data/ann-minist_2layer_BP.train')

    # 크기가 512, 512 이고 int8 형
    dst = np.zeros(shape=(512, 512, 3), dtype=np.uint8)

    # 이미지의 가장 바깥쪽의 contour 만 추출
    mode = cv2.RETR_EXTERNAL
    method = cv2.CHAIN_APPROX_SIMPLE
    font = cv2.FONT_HERSHEY_SIMPLEX
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
    def edgePrint(cls):
        print('left: {}\nright: {}\nup: {}\ndown: {}'.format(cls.leftEdge, cls.rightEdge, cls.upEdge, cls.downEdge))

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
        cv2.imshow('dst', cls.dst)
        cv2.setMouseCallback('dst', cls.onMouse)

    @classmethod
    def mainMethod(cls):
        cls.viewWindow()
        while True:
            key = cv2.waitKey(25)

            if key == 27:
                break

            elif key == ord('q'):
                cls.resetEdge()
                cls.dst[:, :] = 0
                cv2.imshow('dst', cls.dst)

            elif key == ord(' '):
                cls.edgePrint()
                gray = cv2.cvtColor(cls.dst, cv2.COLOR_BGR2GRAY)
                contours, _ = cv2.findContours(gray, cls.mode, cls.method)

                for i, cnt in enumerate(contours):
                    # 3-1
                    x, y, width, height = cv2.boundingRect(cnt)

                    cv2.rectangle(cls.dst, (cls.leftEdge - cls.radius, cls.upEdge - cls.radius),
                                  (cls.rightEdge + cls.radius, cls.downEdge + cls.radius), (0, 0, 255), 2)
                    cx, cy = x + width / 2, y + height / 2

                    if width > height:
                        r = width / 2
                    else:
                        r = height / 2

                    cx, cy, r = int(cx), int(cy), int(r)
                    img = gray[cy - r:cy + r, cx - r:cx + r]
                    img = cv2.resize(img, dsize=(20, 20), interpolation=cv2.INTER_AREA)
                    cls.x_img[:, :] = 0
                    cls.x_img[4:24, 4:24] = img
                    cls.x_img = cv2.dilate(cls.x_img, None, 2)
                    cls.x_img = cv2.erode(cls.x_img, None, 4)
                    cv2.imshow('x_img', cls.x_img)
                    # 3-2
                    x_test = np.float32(cls.x_img.flatten())
                    _, res = cls.ann.predict(x_test.reshape(-1, 784))
                    ##            print('res=', res)
                    y_predict = np.argmax(res, axis=1)
                    print('y_predict=', y_predict)
                    digit = int(y_predict[0])
                    cv2.putText(cls.dst, str(digit), (x, y), cls.font, 3, (255, 0, 0), 5)

                cv2.imshow('dst', cls.dst)
        cv2.destroyAllWindows()


# CharacterRecognition

CharacterRecognition.mainMethod()
