# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 16:05:54 2018

@author: Sophia
"""

import v04


id_list = ['Q1','Q2','Q3']
question_data = {}


for elem in id_list: 
    question_data[elem] = readExamples(elem)
