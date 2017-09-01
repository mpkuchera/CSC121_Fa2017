#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 09:03:34 2017

@author: M.P. Kuchera

@brief: This code serves as the timer for our in-class
        quizzes
"""
import time
import os

minutes = 15.0
tot_time = minutes * 60
output_interval = 5*60 # 5 min in seconds


print "Starting quiz."
for t in range(0,int(tot_time/output_interval)):
    time.sleep(output_interval)
    print (t*output_interval+output_interval)/60.0, "minutes elapsed.\n"
    

print "Time is up."
os.system('say "Time is up."')

    


