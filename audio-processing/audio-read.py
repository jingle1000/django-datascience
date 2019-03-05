import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.io import wavfile
from glob import glob
import librosa

#a string plot title and a numpyArray as parameters
def plot_filter_bank(pltTitle, audioArray):
  fig, axes = plt.subplots()
  fig.suptitle('Filter Bank Coefficients', size=16)
  axes.set_title(pltTitle)
  axes.imshow(list(audioArray, cmap='hot', interpolation='nearest'))
  axes.get_xaxis().set_visible(False)
  axes.get_yaxis().set_visible(False)
  plt.show()

  
#import the source file
#audio_file represents a list of filenames
audio_file = glob('./*.wav')

#fs(int) = sample rate, data(numpy array)
fs, data = wavfile.read(audio_file[0])
#read in the first audio file, create the time array (timeline)
#audio file (numpy array) and frequency (int) in seconds
audio, sfreq = librosa.load(audio_file[0], sr=fs)
time_line = np.arange(0, len(audio)) / sfreq
#bank represents the filter bank coefficients in a numpy array


#create the plot
fig, axes = plt.subplots()
#plot time on the x axis, audio array data on the y axis
axes.plot(time_line, audio)
axes.set(xlabel="Time (s)", ylabel="Sound Amplitude")
plt.show()