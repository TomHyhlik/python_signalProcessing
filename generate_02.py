#!/usr/bin/env python3
import numpy as np
from scipy.io import wavfile

FILENAME_OUT = './wavSamples/sine.wav'
sampleRate = 44100
frequency = 100
length = 2

t = np.linspace(0, length, sampleRate * length) # Produces a 2 second Audio - File

y = np.sin(frequency * 2 * np.pi * t) # Has frequency of 440 Hz

z = np.exp(2) 

y = y * z

wavfile.write(FILENAME_OUT, sampleRate, y)

