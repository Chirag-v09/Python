# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 11:13:36 2020

@author: Chirag
"""

import cv2

img = cv2.imread("Mahindra.jpg")
img = image
img = cv2.resize(img, (700, 500))
img = cv2.line(img, (0, 0), (100, 200), (255, 255, 255), 2)
img = cv2.arrowedLine(img, (10, 255), (255, 100), (255, 0, 255), 2)
img = cv2.rectangle(img, (255, 255), (500, 500), 2)
'''                image, starting ending thickness '''
img = cv2.circle(img, (255, 255), 100, (255, 0, 0), -1)
'''                     if we guive thickness = -1 then the circle we get filled '''
cv2.imshow("Image", img)
cv2.waitkey()
cv2.destroyAllWindows()