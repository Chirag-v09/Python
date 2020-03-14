# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 13:07:00 2020

@author: Chirag
"""

import cv2
cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # Here Width can also be determined by 3
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # Here Height can also be determined by 4
cap.set(3, 700)
cap.set(4, 600)
ret, frame = cap.read()
print(cap.get(3))
print(cap.get(4))
cap.release()