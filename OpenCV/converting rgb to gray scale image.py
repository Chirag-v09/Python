# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 18:02:21 2019

@author: Chirag
"""


import cv2
import glob

till gmc_sierra_1500_2011

images = [cv2.imread(file) for file in glob.glob("SubsetVMMR\gmc_sierra_1500_2011\*.jpg")]

cv2.imshow("Hello", images[0])
cv2.waitKey(0)
cv2.destroyAllWindows()


gray_image = []
for i in range(len(images)):
    gm = cv2.cvtColor(images[i], cv2.COLOR_BGR2GRAY)
    gray_image.append(gm)

cv2.imshow("Gray Image", gray_image[0])
cv2.waitKey(0)
cv2.destroyAllWindows()

for i in range(len(images)):
    gm = gray_image[i]
    nameg = "CAR " + str(i) + ".jpg"
    cv2.imwrite(nameg, gm)

a = images[0]
a1 = a.shape[0]
a2 = a.shape[1]
a3 = a.shape[2]

for i in range(len(images)):
    a = images[i]
    if( a1 > a.shape[0]):
        a1 = a.shape[0]
    if( a2 > a.shape[1]):
        a2 = a.shape[1]
    if( a3 > a.shape[2]):
        a3 = a.shape[2]



img = cv2.imread('00A0A_lm89jTRn6pP_600x450.jpg')
cv2.imshow("Hello", img)
cv2.waitKey(0)
cv2.destroyAllWindows()









contents = dir('*.jpg')
h = contents(1).name
type(contents)

contents = dir('*.jpg') % or whatever the filename extension is
for i = 1:numel(contents)
  filename = contents(i).name;
  % Open the file specified in filename, do your processing...
  [path name] = rgb2gray(filename);
  out_filename = sprintf('%s.jpg', name);
  % write jpg output to 'out_filename'
  fprintf(1, 'Writing %s\n', out_filename);
end