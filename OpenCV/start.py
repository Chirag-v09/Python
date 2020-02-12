# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 17:13:31 2019

@author: Chirag
"""

import cv2
print(cv2.__version__)

imgpath = "4.1.01.tiff"
img = cv2.imread(imgpath)

# Hello is used for naming the window
cv2.imshow("Hello", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# We us ewait key becoz when we just press any kry at that time the window is destroy by using
# this function i.e destroyalllwindows
# if we don't write the wait key  then the window is automatically destroy instantly

# waitkey - i.e waiting for keyboard event.

# named window will create a window and then imgshow function show thw img image in the window
# named "Hello" else it will create a new window.
cv2.namedWindow("Hello", cv2.WINDOW_AUTOSIZE)
cv2.imshow("Hello", img)
cv2.waitKey(0)
cv2.destroyWindow("Hello")
# This time we have control on the window that which window we want to destroy by writing that
# window name in the parenthesis of the destroy function.

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
