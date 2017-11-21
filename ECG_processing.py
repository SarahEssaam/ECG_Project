import filters
import numpy as np
import matplotlib.pyplot as plt

class ECG_Processing:
    """class that does the processing over raw ECG"""
    def __init__(self, dataFile,fs=256):
        file = open(dataFile, 'r')
        signal_strings = file.read().split('\n')
        self.signal_init = np.asarray(signal_strings,dtype=np.float)
        self.signal_filtered = None
        file.close()
        self.fs = fs
    def noise_filtering(self):
        #Apply a bandpass filter of 0.1 to 45 Hz band
        #The Bps is of order 5 so the notch filter of 60 Hz is not important
        self.signal_filtered = filters.notch_Filter(self.signal_init,freq=50,fs=self.fs)
        self.signal_filtered = filters.butter_bandpass_filter(self.signal_filtered,0.1,45,self.fs)
        return self.signal_filtered
    def process_signal(self, N, noise=0):
        #need to check first whether to process the filtered signal or the initial signal
        if noise==0:
            #if you'll use the filtered signal make sure it is not None
            if(self.signal_filtered is None):
                signal = self.noise_filtering()
            else:
                signal = self.signal_filtered
        else:
            signal = self.signal_init
    #1)Differentiate
        signal = self.__differentiate(signal)
    #2)Square
        signal = np.square(signal)
    #3)Smooth
        signal = self.__smooth(signal,N)
    #4)Apply Threshold
        return signal , self.__threshold(signal)
    def __differentiate(self,signal):
        #5 points differentiating method
        kernel = np.array([-1,-2,0,2,1])
        signal_diff = np.zeros_like(signal)
        signal = np.insert(signal,0,[0,0])
        signal = np.append(signal,[0,0])
        den = (1/8)*self.fs
        for i in range(signal_diff.size):
            signal_diff[i] = np.sum(kernel*signal[i:i+5])*den
        return signal_diff

    def __smooth(self,signal,N):
        kernel = np.ones(N,dtype=float)*(1/N)
        signal_smoothed = np.zeros_like(signal)
        signal = np.append(signal,np.zeros(N-1))
        for i in range(signal_smoothed.size):
            signal_smoothed[i] = np.sum(signal[i:i+N]*kernel)
        return signal_smoothed


    def __threshold(self,signal):
        #About 30% abouve the mean line
        #the mean line is like a base line above the noise
        #This is mostly effective in the case of noisy signal where there is an offset to the signal
        threshold = (np.max(signal)-np.mean(signal))*0.3 + np.mean(signal)
        array_above_indices = np.where(signal>threshold)
        time_stamps = np.array([],dtype=np.float)
        prev_i = array_above_indices[0][0] - 1
        dict = {}
        for i in array_above_indices[0]:
            if ((i - prev_i) == 1) or ((i-prev_i)==2): #the secind check is a fix for a bug in np.where
                dict[i] = signal[i]
            else :
                if dict =={} :
                    dict[i]=signal[i]
                index = max(dict, key =dict.get)
                time_stamps = np.append(time_stamps, float(index / self.fs))
                dict = {}
            prev_i = i
        return time_stamps

    def RR_compute(self,time_stamps):
        RR = time_stamps[1:None]
        RR = RR - time_stamps[0:-1]
        return RR

    # Q2 : we want to have an estimate of the longest possible R_R
    # knowing that the R_R interval is between 0.6 to 1 sec (100 to 60 bpm) for a normal person
    # severeal sources claim resting heart beat may be as low as 40 or 50 for athletes
    # so we will use 40 bpm as our threshold -> 1.5 sec

    def sinus_arrest_detect(self, RR, time_stamps):
        # mb for missing beats
        mb_start_indices = np.where(RR > 1.5)
        mb_RR = RR[RR > 1.5]
        mb_start_times = time_stamps[mb_start_indices]
        mb_times = mb_RR / 2 + mb_start_times
        return mb_times