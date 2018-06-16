from scipy import signal
import numpy as np 
import matplotlib.pyplot as plt
import csv

f1 = 10
f2 = 20
f3 = 30

fs = 128
N = 200
time = np.arange(N)/float(fs)
nfft=fs
nperseg=fs

def csvReader(filePath):
    with open(filePath, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='\r')
        dataSource = []

        for row in spamreader:
            dataSource.append(int(row[0]))
        dataSource = np.resize(np.array(dataSource), 600)


        fs1, t, psa = signal.spectrogram(dataSource, fs=fs, nfft=nfft, nperseg=nperseg)
        return dataSource, psa

""" s1 = 1 * np.cos(2*np.pi*time*f1)
s2 = 2 * np.cos(2*np.pi*time*f2)
s3 = 3 * np.cos(2*np.pi*time*f3) """

s1, ps1 = csvReader("D:\\noela\\Documents\\3TI\\TFE\\github\\csv\\csvCleanData\\winkLeft\\winkLeft11Data\\AF3.csv")
s2, ps1 = csvReader("D:\\noela\\Documents\\3TI\\TFE\\github\\csv\\csvCleanData\\winkLeft\\winkLeft11Data\\F3.csv")
s3, ps1 = csvReader("D:\\noela\\Documents\\3TI\\TFE\\github\\csv\\csvCleanData\\winkLeft\\winkLeft11Data\\F7.csv")

fs1, ts1, sx1 = signal.spectrogram(s1, fs=fs, nfft=nfft, nperseg=nperseg)
fs2, ts2, sx2 = signal.spectrogram(s2, fs=fs, nfft=nfft, nperseg=nperseg)
fs3, ts3, sx3 = signal.spectrogram(s3, fs=fs, nfft=nfft, nperseg=nperseg)

fp1, sp1 = signal.periodogram(s1, fs=fs, nfft=nfft, scaling='spectrum')
fp2, sp2 = signal.periodogram(s2, fs=fs, nfft=nfft, scaling='spectrum')
fp3, sp3 = signal.periodogram(s3, fs=fs, nfft=nfft, scaling='spectrum')

""" ac1 = np.correlate(s1, s1, mode='full')
ac1 = np.resize(ac1, 600)
ac1fft = np.fft.rfft(ac1)
ac1fft = np.square(ac1fft) """


plt.subplot(411)
plt.plot(s1, color='red')
plt.plot(s2, color='green')
plt.plot(s3, color='blue')
plt.title('signaux sources')

plt.subplot(412)
plt.plot(sx1, color='red')
#plt.plot(sx2, color='green')
#plt.plot(sx3, color='blue')

plt.subplot(413)
plt.plot(sp1, color='red')
plt.plot(sp2, color='green')
plt.plot(sp3, color='blue')

""" plt.subplot(413)
plt.plot(ac1, color='red')

plt.subplot(414)
plt.plot(ac1fft, color='blue') """

plt.subplots_adjust(0.09, 0.04, 0.94, 0.94, 0.26, 0.46)
plt.show()