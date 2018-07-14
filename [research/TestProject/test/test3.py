# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 11:17:50 2018

@author: Anjali
"""

values = [ (True, 0.9624781131744384),(True, 0.9170554161071778),(False, 0) ]
total = 0
for elem in values:
    print(elem)
    if elem[0] == True:
       total += 1
print (total)       

lans = sum(elem[0] for elem in values)

