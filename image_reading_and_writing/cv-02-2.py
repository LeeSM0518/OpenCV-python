import numpy as np
import cv2
import matplotlib.pyplot as plt

def showImage() :
    imgfile = '../data/image.png'

    # 이미지를 회색으로 불러움
    img = cv2.imread(imgfile, cv2.IMREAD_GRAYSCALE)

    # imshow 이미지를 디스플레이 하는 방법
    plt.imshow(img, cmap='gray', interpolation='bicubic')

    # x축 t축으로 눈금 표시
    # 눈금 표시 없이 이미지를 표시하라는 코드
    plt.xticks([])
    plt.yticks([])
    plt.title('Jeny')

    # 이미지 출력
    plt.show()

showImage()