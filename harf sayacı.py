#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 16:03:18 2024

@author: ugurburak
"""

import numpy as np 

import matplotlib as plt


s = "Uğur Burak Berber."
 
print("boşluklu harf sayısı",len(s))
t = 0
for i in range (len(s)):
    if s[i] !=  " " :
        t += 1
print("boşluksuz harf sayısı", t)
t = 0
for i in range (len(s)):
    if s[i] not in [" ", ".",",",":",";","!"]:
        t += 1
print("sadece harf sayısı", t)
ss = s.split(" ")

s2 = []
s1 = ""
for i in range(len(s)):
    if s[i] not in [" ", ".",",",":",";","!"]:
        s1 += s[i]
    else:
        s2.append(s1)
        s1 = ""
        
