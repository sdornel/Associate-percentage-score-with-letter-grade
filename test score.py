# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 16:23:19 2020

@author: kai_d
"""


score = float(input("Please enter a score between 0.0 and 1.0: "))
while score > 1.0 or score < 0:
    score = float(input("Enter a score between 0.0 and 1.0: "))
if score > .9:
    print("A")
elif score > .8:
    print("B")
elif score > .7:
    print("C")
elif score > .6:
    print("D")
elif score < .6 and score > .000001:
    print("F")