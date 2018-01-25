im# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
""
import cv2
import numpy as np

def is_inside(o,i):
    ox,oy,ow,oh=o
    ix,iy,iw,ih=i
    return ox>ix and oy>iy and ox+ow<ix+iw and oy+oh<iy+ih

def draw_person(image,person):
    x,y,w,h=person
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)


img=cv2.imread(r'C:\Users\zylzlh\Desktop\1.jpg',0)
hog=cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
found,w=hog.detectMultiScale(img)
found_filter=[]
for ri,r in enumerate(found):
    for qi,q in enumerate(found):
        if ri!=qi and is_inside(r,q):
            break
        else:
            found_filter.append(r)
for person in found_filter:
    draw_person(img,person)
cv2.imshow("person detection",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

    