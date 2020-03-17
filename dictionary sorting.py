# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 15:55:13 2020

@author: Chirag
"""


d = {'a': 1, 'b': 2, 'c': 5, 'd': 4, 'e': 3}
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
{k: v for k, v in sorted(d.items(), key=lambda item: item[1])}


d.keys()
for a in sorted(d.keys()):
    print(a)


def dict_val(x):
    return x[1]
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=dict_val)

for key, values in d.items():
    print(key, values)


text = "Chirag"
d = {}
for letter in text:
    
    if letter in d.keys():
        d[letter] += 1
    else:
        d[letter] = 1