import matplotlib.pyplot as plt
from scipy.io.wavfile import read as readwav
import numpy as np

rate_mobile, y_mobile = readwav("C:\\Users\\kieri\\OneDrive\\Documents\\Istrakon 2019\\Mobile phone audio track.wav")
rate_camera, y_camera = readwav("C:\\Users\\kieri\\OneDrive\\Documents\\Istrakon 2019\\Camera merged audio track.wav")

time_mobile = np.arange(0, np.floor(float(len(y_mobile) / 100.0)), 1) / (float(rate_mobile) / 100.0)
y_mobile_ss = y_mobile[0 : int(np.floor(float(len(y_mobile) / 100.0)) * 100) : 100]
time_camera = np.arange(0, np.floor(float(len(y_camera) / 100.0)), 1) / (float(rate_camera) / 100.0)
y_camera_ss = y_camera[0: int(np.floor(float(len(y_camera) / 100.0)) * 100) : 100]

plt.figure(1)
plt.subplot(211)
plt.plot(time_mobile, y_mobile_ss, linewidth=0.02, alpha=1.0, color="#ff7f00")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.subplot(212)
plt.plot(time_camera, y_camera_ss, linewidth=0.02, alpha=1.0, color="#ff7f00")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()