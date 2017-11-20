import matplotlib.pyplot as plt
from ECG_processing import ECG_Processing
from plotting import plot

ecg = ECG_Processing('Data2.txt')
plot.counter = 0
'''
sig,timeS = e.process_signal(20)
plot(sig,time_stamps=timeS,end = 1000)
R_R = e.RR_compute(time_stamps=timeS)
plot(R_R)
print(e.sinus_arrest_detect(R_R,timeS))
plot(sig,time_stamps=e.sinus_arrest_detect(R_R,timeS),start=2000,end=3000)
'''
final_sig, time_stamps = ecg.process_signal(N=25,noise=1)
plot(final_sig,time_stamps,end=2000)
final_sig, time_stamps = ecg.process_signal(N=25,noise=0)
plot(final_sig,time_stamps,end=2000)
plt.show()