im# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
""
import cv2
import numpy as np
def read_img():
    X,Y=[],[]
    f=open(r'D:\opencv_work\train.csv','r')
    for i in f:
        x,y=i.split(',')
        im=cv2.imread(x,0)
        X.append(np.asarray(im,dtype=np.uint8))
        Y.append(y)
    return [X,Y]

names=['zheng','wang','yang']
[X,Y]=read_img()
y=np.asarray(Y,dtype=np.int32)
model=cv2.face.createEigenFaceRecognizer()
model.train(np.asarray(X),np.asarray(y))
face_cascade=cv2.CascadeClassifier(r'D:\opencv_work\cascades\haarcascade_frontalface_default.xml')
camera=cv2.VideoCapture(0)
while True:
    read, frame = camera.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        img=cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi=gray[y:y+h,x:x+w]
        try:
            roi=cv2.resize(roi,(200,200),interpolation=cv2.INTER_LINEAR)
            params=model.predict(roi)
            print('Label:{0}, Confidence:{1:.2f}'.format(params[0],params[1]))
            cv2.putText(frame,names[params[0]],(x,y-20),cv2.FONT_HERSHEY_SIMPLEX,1,255,2)
        except:
            continue
    cv2.imshow('camera',frame)
    if cv2.waitKey(30) & 0xff ==27:
        break
camera.release()
cv2.destroyAllWindows()
    