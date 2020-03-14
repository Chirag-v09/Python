# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 11:03:32 2020

@author: Chirag
"""

import cv2


img = cv2.imread("mahindra.jpg")
img = image
img = cv2.resize(img, (640, 420))
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img, "Hello", (10, 400), font, 2, (255, 255, 255), 4, cv2.LINE_8)

cv2.imshow("Image", img)
cv2.waitKey()
