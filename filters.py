from scipy.signal import butter, lfilter, iirnotch


def butter_bandpass_filter(data, lowcut, highcut, fs=256, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    filtered_data = lfilter(b, a, data)
    return filtered_data

def notch_Filter(data, Q=35, fs= 256,freq=50):
    nyq = fs/2
    f0 = freq / nyq
    b, a = iirnotch(f0,Q)
    filtered_data = lfilter(b, a, data)
    return filtered_data