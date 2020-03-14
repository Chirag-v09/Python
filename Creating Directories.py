# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 20:49:16 2020

@author: Chirag
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

directory = "Folder1"

parent_dir = "E:/"

path = os.path.join(parent_dir, directory)

os.mkdir(path)


# Parent Directory path 
parent_dir = "E:/New Folder"
  
# mode 
mode = 0o666
  
# Path 
path = os.path.join(parent_dir, directory) 
  
# Create the directory 
# 'GeeksForGeeks' in 
# '/home / User / Documents' 
# with mode 0o666 
os.mkdir(path, mode) 
print("Directory '% s' created" % directory)
