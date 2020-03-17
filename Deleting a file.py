# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 10:15:36 2020

@author: Chirag
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import glob
import os

files = [file for file in glob.glob("*")]
for file in files:
    os.remove(file)

# Hence Delete all file in files
