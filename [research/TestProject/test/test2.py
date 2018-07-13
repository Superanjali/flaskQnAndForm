# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 07:12:48 2018

@author: Sophia
"""


class Globals():
    def __init__(self):
        self.question_list = ['is anjali cute?','Are you crazy?','What do you want?']
        self.state = -2 #assume the last page with the end test so the next page is start test
        self.name = ''
        self.score = ''
        self.question = ''
        self.reply = ''
    def __setattr__(self,key,value):
        self.__dict__[key] = value
    def to_dict(self):
        return self.__dict__

g = Globals()
g.newkey = 5
print(g.state)
print(g.to_dict())