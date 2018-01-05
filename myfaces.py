im# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
""
import cv2
import numpy as np
face_cascade=cv2.CascadeClassifier(r'D:\opencv_work\cascades\haarcascade_frontalface_default.xml')
count=0
camera=cv2.VideoCapture(0)
while True:
    ret, frame = camera.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        img=cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        f=cv2.resize(gray[y:y+h,x:x+w],(200,200))
        cv2.imwrite('D:\opencv_work\zyl\%s.pgm' % str(count),f)
        count+=1
    cv2.imshow('camera',frame)
    if cv2.waitKey(30) & 0xff ==27:
        break
camera.release()
cv2.destroyAllWindows()
        
    