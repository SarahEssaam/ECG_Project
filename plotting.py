import matplotlib.pyplot as plt
import numpy as np

def plot(signal,time_stamps=None,T=1/256):
    plt.figure(plot.counter)
    plot.counter += 1
    if np.all(time_stamps) != None:
        R_index = np.array((time_stamps/T),dtype=np.int)
        R_index = R_index[R_index < signal.shape[0]]
        plt.plot(R_index,signal[R_index], marker='*', linestyle='None', color='r')
    plt.plot(signal, linestyle='-', color='k')

