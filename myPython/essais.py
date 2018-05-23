from scipy import signal
import numpy as np
import csv

with open('.\\csv\\csvCleanData\\neutral\\neutral1Data\\AF3.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\r')
    dataSource = []
    strData = ''

    fs = 128
    nfft = 64

    for row in spamreader:
         dataSource.append(int(row[0]))
    dataSource = np.array(dataSource)

    frequencySample, powerSpectralArray = signal.periodogram(dataSource, fs, nfft=nfft)

    for l in range(1, 4):
        strData += '{:4}'.format(str(powerSpectralArray[l])) + ', '

    print(strData)