import matplotlib.pyplot as plt
import numpy as np

def plot(signal,time_stamps=None,T=1/256,start=0,end=None):
    plt.figure(plot.counter)
    plot.counter += 1
    if end == None:
        end = signal.shape[0]
    if np.all(time_stamps) != None:
        R_index = np.array((time_stamps/T),dtype=np.int)
        R_index = R_index[R_index >= start]
        R_index = R_index[R_index < end]
        plt.plot(R_index,signal[R_index], marker='*', linestyle='None', color='r')
#        plt.plot(R_index, np.max(signal[R_index])*np.ones(R_index.shape[0]), marker='*', linestyle='None', color='r')
    plt.plot(range(start,end),signal[start:end], linestyle='-', color='k')
