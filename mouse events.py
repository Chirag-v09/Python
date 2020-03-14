# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 13:33:44 2020

@author: Chirag
"""

import cv2

image = cv2.imread("mahindra.jpg")
events = [i for i in dir(cv2) if "EVENT" in i]
image = cv2.resize(image, (500, 500))

cv2.imshow("image1", image)
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
    
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = image[x, y, 0]
        green = image[x, y, 1]
        red = image[x, y, 2]
        print("image")
        rgb.append([red, green, blue])


cv2.setMouseCallback("image", click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()

