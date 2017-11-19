import numpy as np
import matplotlib.pyplot as plt
from ECG_processing import ECG_Processing
from plotting import plot


e = ECG_Processing('Data2.txt')
#plt.subplot(1,2,1)
plot.counter = 0

plot(e.signal_init[:500])
plot(e.noise_filtering()[:500])
plot(e.process_signal(20)[:500],np.array([0,216.3,440.951])/256)
plt.show()
'''
x = np.arange(5)
y = np.exp(x)
plt.figure(0)
plt.plot(x, y)

z = np.sin(x)
plt.figure(1)
plt.plot(x, z)

w = np.cos(x)
plt.figure(0) # Here's the part I need
plt.plot(x, w)
plt.show()
'''