# 이미지 픽셀 조작 및 ROI 조작

## 픽셀 및 ROI

* **코드**

  ```python
  import numpy as np
  import cv2
  
  img = cv2.imread('../data/image.png')
  # 이미지의 (340, 200) 위치의 픽셀 값을 추출
  px = img[340, 200]
  print(px)
  # 실행결과 : [ 62 117 151]
  # Blue=62, Green=117, Red=151
  
  # BGR 을 하나씩 추출해서 따로 저장
  B = img.item(340, 200, 0)
  G = img.item(340, 200, 1)
  R = img.item(340, 200, 2)
  
  BGR = [B, G, R]
  print(BGR)
  
  # img.itemset((340, 200, 0), 100)
  # : (340, 200) 위치의 픽셀의 Blue 값을 100으로 변경
  
  # 이미지 속성 얻기
  print(img.shape)    # (1710, 1268, 3)
  print(img.size)     # 6504840
  print(img.dtype)    # uint8
  
  # 원본 이미지 출력
  cv2.imshow('original', img)
  
  # 300~400 : 세로
  # 350~750 : 가로
  subimg = img[300:400, 350:750]
  cv2.imshow('cutting', subimg)
  
  # 원본 이미지의 좌표 (0, 300)~(400, 400) 영역에
  # subimg 삽입
  img[300:400, 0:400] = subimg
  
  print()
  print(img.shape)
  print(subimg.shape)
  
  cv2.imshow('modified', img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  ```



## 이미지 채널 분할 및 합치기

* **코드**

  ```python
  import numpy as np
  import cv2
  
  img = cv2.imread('../data/image.png')
  
  # B, G, R 채널별로 분리 후 저장
  b, g, r = cv2.split(img)
  
  # 100, 100 위치의 B, G, R 출력
  print(img[100, 100])
  print(b[100, 100], g[100, 100], r[100, 100])
  
  # B, G, R 이미지 출력
  cv2.imshow('blue channel', b)
  cv2.imshow('green channel', g)
  cv2.imshow('red channel', r)
  
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  ```

  