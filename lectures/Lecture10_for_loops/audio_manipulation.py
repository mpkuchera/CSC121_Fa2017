#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 08:25:46 2017
@file: audio_manipulation.py

@author: M.P. Kuchera
@breif: This program decreases the volume of an audio sample

***TASK****
1. loop over an audio sample and decrease the volume by a given factor.
2. play the audio before and after manipulation

***********

"""

# audio.py must be in the same folder as this file or installed on your computer
import audio 



def make_softer(audio_file):

    
    # the following function will play the .wav file
    audio.play(audio_file)
    
    # storing the audio as a list of floats
    samples = audio.read_wav(audio_file)
    
    
    # add code here!!!!
    
    
    
    # write a list as a .wav file
    #audio.write_wav(louder_audio, 'louder.wav') 
    
    # play the new sound file that was just saved.
    #audio.play('louder.wav')
    
def main():
    # the following files must be in the same folder as this file
    #audio_file = 'drums.wav' 
    audio_file = 'synth.wav'
    make_softer(audio_file)