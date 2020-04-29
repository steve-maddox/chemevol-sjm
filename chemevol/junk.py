#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 22:03:11 2020

@author: stephenmaddox
"""
import sys 

for ii in range(10): 
    print(ii) 
    if(ii>5): 
        sys.exit(0) 
        print('should have stopped')

        