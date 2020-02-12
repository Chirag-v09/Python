# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 09:02:34 2020

@author: Chirag
"""


from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cv2
import glob
import argparse
import random as rng

rng.seed(12345)

def thresh_callback(val):
    threshold = val
    
    canny_output = cv2.Canny(src_gray, threshold, threshold * 2)
    
    
    contours, hierarchy = cv2.findContours(canny_output, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    
    contours_poly = [None]*len(contours)
    boundRect = [None]*len(contours)
    centers = [None]*len(contours)
    radius = [None]*len(contours)
    for i, c in enumerate(contours):
        contours_poly[i] = cv2.approxPolyDP(c, 3, True)
        boundRect[i] = cv2.boundingRect(contours_poly[i])
        centers[i], radius[i] = cv2.minEnclosingCircle(contours_poly[i])
    
    
    drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
    
    

    for i in range(len(contours)):
        color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
        cv2.drawContours(drawing, contours_poly, i, color)
        cv2.rectangle(drawing, (int(boundRect[i][0]), int(boundRect[i][1])), \
          (int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])), color, 2)
        # cv2.circle(drawing, (int(centers[i][0]), int(centers[i][1])), int(radius[i]), color, 2)
    
    
    cv2.imshow('Contours', drawing)



########### Main Code :-
src = cv2.imread('mahindra1.jpg')
src_gray = cv2.imread('mahindra1.jpg', 0)# by putting 0 image will read as a gray scale image

# =============================================================================
# cv2.imshow("winname", src)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# =============================================================================

src_gray_blur = cv2.blur(src_gray, (3,3))

# =============================================================================
# cv2.imshow("winname", src_gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# =============================================================================

source_window = 'Source'
cv2.namedWindow(source_window)
cv2.imshow(source_window, src)

max_thresh = 255
thresh = 100 # initial threshold
cv2.createTrackbar('Canny thresh:', source_window, thresh, max_thresh, thresh_callback)
thresh_callback(thresh)

cv2.waitKey()