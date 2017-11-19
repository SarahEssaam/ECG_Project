import numpy as np
import itertools
import matplotlib.pyplot as plt
from ECG_processing import ECG_Processing
from plotting import plot

'''
a = np.arange(10)+10
ind = np.where(a>14)
for i in ind:
    print (a[i])
for (i,v) in itertools.zip_longest(np.ndindex(a.shape),a):
    print(i[0]+1,v)
'''
e = ECG_Processing('DataN.txt')

plot.counter = 0
e.signal_init[:500]
e.noise_filtering()[:500]
sig,timeS = e.process_signal(20)
plot(sig[:500],time_stamps=timeS)
#plot(signal=sig,time_stamps=timeS)
plot(e.RR_compute(time_stamps=timeS))
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