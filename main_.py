#1) A figure showing the first 2000 samples of the ECG signal before and after noise filtering. Name the figure “Before_After_Filter.jpg”"
#First import The Class ECG_Processing that handles all the required functions, and plot function that plots the data as required"
import matplotlib.pyplot as plt
from ECG_processing import ECG_Processing
from plotting import plot
#Create instance from class \n",
ecg = ECG_Processing(dataFile='DataN.txt',fs=256)
#initialize counter for plotted figures
plot.counter = 0
plot(signal=ecg.signal_init,start=0,end=2000)
#plot the filtered signal in blue
plt.plot(ecg.noise_filtering()[:2000], linestyle='--', color='b')
#Additionally plotting one QRS wave
#plot(ecg.signal_filtered,start=480,end=520)

#2) A figure showing the first 2000 samples of the ECG signal with an “*” marking the detected R waves for N= 5. Name the figure “DetectedR_5.jpg”"
final_sig, time_stamps = ecg.process_signal(N=5)
plot(final_sig,time_stamps,end=2000)
#Additionally plotting one QRS wave
#plot(final_sig,time_stamps,start=450,end=550)
#3) A figure showing the first 2000 samples of the ECG signal with an “*” marking the detected R waves for N= 15. Name the figure “DetectedR_15.jpg”"
final_sig, time_stamps = ecg.process_signal(N=15)
plot(final_sig,time_stamps,start=0,end=2000)
#plot(final_sig,time_stamps,start=450,end=550)

#Additionallly plotting for N=20\n",
final_sig, time_stamps = ecg.process_signal(N=20)
plot(final_sig,time_stamps,start=0,end=2000)
#plot(final_sig,time_stamps,start=450,end=550)

#4) A figure showing the first 2000 samples of the ECG signal with an “*” marking the detected R waves for N= 25. Name the figure “DetectedR_25.jpg”"
final_sig, time_stamps = ecg.process_signal(N=25)
plot(final_sig,time_stamps,end=2000)
#plot(final_sig,time_stamps,start=450,end=550)

#5) What you can conclude about the optimal setting of N?"
#"Answer : A range from 15 to 20 samples seems to be most precise, as that number increase the width of the given QRS signal increases, so the detection of R wouldn't be precise, and as the number decreases the QRS is not smoothed well enough into one peak. The number seems to be the same of the width of the QRS signal.

#6) A figure showing the first 2000 samples of the ECG signal with an “*” marking the detected R waves for N= 25 But without noise filtering. Name the figure “Unfiltered_25.jpg”"
final_sig, time_stamps = ecg.process_signal(N=25,noise=1)
plot(final_sig,time_stamps,end=2000)

#7) A plot of the RR intervals with Beat number on the x-axis and RR interval in msec on the y-axis in the case of N= 25. Name the figure “RR.jpg”"
RR_intervals = ecg.RR_compute(time_stamps)
plot(RR_intervals*1000)

plt.show()