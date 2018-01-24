im# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
""
import cv2
import numpy as np
from matplotlib import pyplot as plt
img2=cv2.imread(r'C:\Users\zylzlh\Desktop\qiuyi.jpg',0)
img1=cv2.imread(r'C:\Users\zylzlh\Desktop\biaozhi.jpg',0)
sift=cv2.xfeatures2d.SIFT_create()
kp1,des1=sift.detectAndCompute(img1,None)
kp2,des2=sift.detectAndCompute(img2,None)
FLANN_INDEX_KDTREE=0
indexParams=dict(algorithm=FLANN_INDEX_KDTREE,tree=5)
searchParams=dict(checks=50)
flann=cv2.FlannBaesdMatcher(indexParams,searchParams)
matches=flann.knnMatch(des1,des2,k=2)
matchesMask=[[0,0] for i in range(len(matches))]
for i,(m,n) in enumerate(matches):
    if m.distance < 0.7*n.distance:
        matchesMask[i]=[1,0]
drawParams=dict(matchColor=(0,255,0),
                singlePointColor=(255,0,0),
                matchesMask=matchesMask,
                flags=0)
resultImage=cv2.drawMatchesKnn(img1,kp1,img2,kp2,matches,
                               None,**drawParams)
plt.imshow(resultImage)
plt.show()
    