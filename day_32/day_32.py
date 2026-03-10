import librosa as lb
import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np

y, sr = lb.load("game_over.wav", sr = None)

print(f"Audio duration: {lb.get_duration(y = y, sr = sr)} seconds")
print(f"Sampling rate: {sr}Hz")

sd.play(y, sr)
sd.wait()

plt.figure(figsize = (10, 4))
lb.display.waveshow(y, sr = sr)
plt.title("waveform")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.show()




# spectrogram
# short-time fourier transform(STFT) -> analyze how the freq will change over the time

d = lb.amplitude_to_db(np.abs(lb.stft(y)), ref = np.max)
plt.figure(figsize = (10, 4))
lb.display.specshow(d, sr = sr, x_axis = "time", y_axis = "log")
plt.title("spectrogram")
plt.show()




# extract mel-frequency cepstral coefficients(MFCCs)

mfccs = lb.feature.mfcc(y = y, sr = sr, n_mfcc = 13)
plt.figure(figsize = (10, 4))
lb.display.specshow(mfccs, sr = sr, x_axis = "time")
plt.title("MFCCs")
plt.show()




# chroma features
# 12 different musical pitch classes: C, C#, D, D#, E, F, F#, G, G#, A, A#, B

chroma = lb.feature.chroma_stft(y = y, sr = sr)
plt.figure(figsize = (10, 4))
lb.display.specshow(chroma, sr = sr, x_axis = "time", y_axis = "chroma")
plt.title("Chroma features")
plt.show()




# tempo(speed of the music) and beats(rhythm)

tempo, beats = lb.beat.beat_track(y = y, sr = sr)
print(f"esitmated tempo: {tempo} BPM")
beat_times = lb.frames_to_time(beats, sr = sr)
plt.figure(figsize = (10, 4))
lb.display.waveshow(y, sr = sr)
plt.vlines(beat_times, ymin = -1, ymax = 1, color = "r", linestyle = "--", label = "Beats")
plt.title("Beat Tracking")
plt.legend()
plt.show()




# zero-crossing rate -> no. of times your audio signal changes from +ve to -ve or -ve to +ve

zcr = lb.feature.zero_crossing_rate(y)
plt.figure(figsize = (10, 4))
plt.plot(zcr[0], label = "zero-crossing rate")
plt.xlabel("Frames")
plt.ylabel("Rate")
plt.title("Zero-Crossing Rate")
plt.legend()
plt.show()




# to reduce the noise

import noisereduce as nr
import soundfile as sf
reduce = nr.reduce_noise(y = y, sr = sr, prop_decrease = 0.8)
sf.write("no_noise.wav", reduce, sr)
