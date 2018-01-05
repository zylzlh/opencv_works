# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 19:37:44 2017

@author: zylzlh
"""

import cv2
import numpy as np
face_cascade=cv2.CascadeClassifier(r'D:\opencv_work\cascades\haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier(r'D:\opencv_work\cascades\haarcascade_eye.xml')
camera=cv2.VideoCapture(0)
while True:
    ret, frame = camera.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        img=cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray=gray[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray,1.03,5,0,(40,40))
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(img,(ex+x,ey+y),(ex+ew+x,ey+eh+y),(0,0,255),2)
    cv2.imshow('camera',frame)
    if cv2.waitKey(30) & 0xff ==27:
        break
camera.release()
cv2.destroyAllWindows()