im# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
""
import cv2
cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter(r'C:\Users\zylzlh\Desktop\1.avi',fourcc,20.0,(640,480))
while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    out.write(frame)
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    if cv2.waitKey(1) & 0xFF==27:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
