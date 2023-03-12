import numpy as np
import cv2

# 얼굴과 눈을 찾기 위한 OpenCV 알고리즘이 적용된 파일
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'C:\python_40\23. Mosaic (OpenCV)\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_eye.xml')

# numpy로 파일 읽어오기
ff= np.fromfile(r'23. Mosaic (OpenCV)\group.jpg', np.uint8)
# imdecode를 하여 numpy의 이미지 파일을 OpenCV 이미지로 불러오기
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)
# 이미지 크기 조절. fx,fy의 비율로 조절
img = cv2.resize(img, dsize=(0,0), fx=1.0, fy=1.0, interpolation=cv2.INTER_LINEAR)

# 이미지에서 얼굴 찾기 위해 회색조 처리
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 여러  개의 얼굴 찾기. 1.2는 ScaleFactor(감도), 5는 minNeighbor(최소이격거리)
# 얼굴 찾아 파란색 네모 표시
faces = face_cascade.detectMultiScale(gray, 1.2,5)
for(x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)

    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    #눈을 찾아 녹색 네모 표시
    for(ex,ey, ew, eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew, ey+eh),(0,255,0),2)

cv2.imshow('face find', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



