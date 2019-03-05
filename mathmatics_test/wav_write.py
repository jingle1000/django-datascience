# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 10:56:47 2019

@author: jingl
"""

import numpy as np
from scipy.io.wavfile import write
import matplotlib.pyplot as plt

def normalize(data):
  signed16 = 32767
  scaled = np.int16(data/np.max(np.abs(data)) * signed16)
  return scaled

data = np.random.uniform(-1, 1, 44100)
scaled = normalize(data)
sinwave = np.sin(np.linspace(0, 10000, 2000000))
sinwave = normalize(sinwave)
x = np.arange(0, len(sinwave), 1)
fig, axes = plt.subplots()
axes.plot(x, sinwave)
plt.show()
write('test.wav', 44100, sinwave)
