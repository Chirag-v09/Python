# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 20:09:19 2019

@author: Chirag
"""


import cv2
import glob

images = [cv2.imread(file) for file in glob.glob("*.jpg")]

cv2.imshow("Hello", images[0])
cv2.waitKey(0)
cv2.destroyAllWindows()

scaled_images = []

for i in range(len(images)):
    img_scaled = cv2.resize(images[i], (512, 256), interpolation = cv2.INTER_AREA)
    scaled_images.append(img_scaled)

for i in range(len(scaled_images)):
    sm = scaled_images[i]
    names = "CAR" + str(i) + "scaled.jpg"
    cv2.imwrite(names, sm)

cv2.imshow("Hello", img_scaled)
cv2.waitKey()

cv2.destroyAllWindows()


######## using with converting rgb to gray scale image file.py
scaled_images = []
for i in range(len(gray_image)):
    img_scaled = cv2.resize(gray_image[i], (150, 150), interpolation = cv2.INTER_AREA)
    scaled_images.append(img_scaled)