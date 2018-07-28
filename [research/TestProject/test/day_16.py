# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 17:37:20 2018

@author: Sophia
"""

#%%
import re
s = str(input())

w = re.search('[a-zA-Z]', s) 
if w != None:
    print('Bad String')
else:
    print(int(s))

# %%
try:
    print(int(input()))
except Exception as e:
    print(e)























