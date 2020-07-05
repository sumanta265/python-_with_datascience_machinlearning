# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 23:10:37 2019

@author: SUMANTA KR MAJI
"""
f= open('untitled1.txt','r')


f1=open('abc.txt','a')

for data in f:
    f1.write(data)

