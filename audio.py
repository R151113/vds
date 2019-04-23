import scipy.io.wavefile as wav
import numpy as np
import matplotlib.pyplot as plot
fs,data=wav.read('voice.wav')
print(fs,len(data),data)
plot.subplot(2,1,1)
plot.plot(data)
t=np.arange(0,len(datas)/fs,1.0/fs)
plot.subplot(2,1,2)
plot.plot(t,data)
plot.show()
wav.write('voice-slow.wav',0.5*fs,data)
