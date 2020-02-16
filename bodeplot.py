#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 13:53:14 2020

@author: kuntal
"""

from pylab import *

def H(w):
    wc = 1e6*pi
    return 2.0/(1.0 + 1j* w / wc)



f = logspace(1,5)

plot(f,20*log10(abs(H(2*pi*f)))); xscale('log')

