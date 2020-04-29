#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 11:35:29 2020

@author: eduardo
"""

from time import sleep

def slow_calculation(cb=None, x=5):
    res = 0
    for i in range(x):
        res += i*i
        sleep(1)
        if cb: cb(i)
    return res

def show_progress(epoch):
    print("Awesome! We've finished epoch {}".format(epoch))


slow_calculation(cb=show_progress, x=3)

#########################################


def slow_calculation2(cb=None):
    res = 0
    for i in range(4):
        res += i*i
        sleep(1)
        if cb: cb(i)
    return res

class ProgressShowingCallback():
    def __init__(self, exclamation="Awesome"):
        self.exclamation = exclamation
        
    def __call__(self, epoch):
        print("{}! We've finished epoch {}!".format(self.exclamation, epoch))
        
cb = ProgressShowingCallback("Just super")

slow_calculation2(cb)

#############################################
        
def f(*args, **kwargs):
    print("args: {}' kwargs: {}".format(args, kwargs))
    
f(3, 'a', thing1="hello")

def slow_calculation3(cb=None):
    res = 0
    for i in range(4):
        if cb: cb.before_calc(i)
        res += i*i
        sleep(1)
        if cb: cb.after_calc(i, val=res)
    return res


        





