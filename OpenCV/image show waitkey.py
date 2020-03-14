# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 09:10:39 2020

@author: Chirag
"""

import cv2

img = cv2.imread("mahindra.jpg")
cv2.imshow("Image", img)
cv2.waitKey()

# To read an image in gray scale format
img = cv2.imread("mahindra.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Image", img)
''' By Pressing 'a' on keyboard all windows will destroy'''
# In this waitKey() return the ASCII value of the charater you entered by keyboard
# So when we press alphabet a the window will get detroyed as it's ASCII value = 97
if cv2.waitKey() == 97 or cv2.waitKey() == -1: # Here -1 value occur when we close the window
    # To destroy a particular window
    cv2.destroyWindow("Image")
    #cv2.destroyAllWindows()

img = cv2.imread("mahindra.jpg")
cv2.imshow("Image", img)
while(1):
    if cv2.waitKey() == 97 or cv2.waitKey() == -1:
        cv2.destroyWindow("Image")
        break

