# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 09:29:07 2019

@author: Chirag
"""
11, 12, 13

from skimage.io import imread_collection

img_dir = "SubsetVMMR\gmc_sierra_1500_2010\*.jpg"

imagess = imread_collection(img_dir)

import cv2
import glob

images = [cv2.imread(file) for file in imagess.files]

images1 = [cv2.imread(file) for file in glob.glob("SubsetVMMR\gmc_sierra_1500_2010\*.jpg")]
