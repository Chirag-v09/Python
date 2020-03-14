# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 19:07:01 2020

@author: Chirag
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cv2
import os
import glob
import math


count = 0
cap = cv2.VideoCapture('video.avi')   # capturing the video from the given path
frameRate = cap.get(5) #frame rate
x=1
while(cap.isOpened()):
    frameId = cap.get(1) #current frame number
    print(frameId)
    # x += 1
    
    ret, frame = cap.read()
    if (ret != True):
        print("hello")
        break
    if (frameId % math.floor(frameRate) == 0):
        # storing the frames in a new folder named train_1
        filename = "frames/_frame%d.jpg" % count
        count+=1
        cv2.imwrite(filename, frame)
cap.release()
