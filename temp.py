im# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
""
import cv2
import numpy as np
img=cv2.imread('C:\Users\zylzlh\Desktop\1.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
dst=cv2.cornerHarris(gray,2,23,0.04)
img[dst>0.01*dst.max()]=[0,0,255]
while True:
    cv2.imshow('corner',img)
    if cv2.waitKey(30) & 0xff ==27:
        break
cv2.destroyAllWindows()
    