import matplotlib.pyplot as plt
from ECG_processing import ECG_Processing
from plotting import plot

ecg = ECG_Processing('DataN.txt')
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
plot(final_sig,time_stamps,start=210,end=240)
plt.savefig('ft1.png')
plot(final_sig,time_stamps,start=0,end=240)
plt.savefig('ft2.png')
#plt.plot(final_sig[:10])
plt.show()