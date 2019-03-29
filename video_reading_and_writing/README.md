# Video Reading and Writing

## 카메라로부터 비디오 캡쳐하기

* **code**

  ```python
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
  ```

  > **비디오 파일 재생하기**
  >
  > cv2.VideoCapture() 함수의 인자로 비디오 파일의 경로를 포함한 파일 이름을 지정하면 된다.



## 비디오 저장하기 또는 녹화하기

* **code**

  ```python
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
  ```

  