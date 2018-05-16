import matplotlib.pyplot as plt
import numpy as np
import csv
import os
from scipy import signal

fileDir = os.getcwd()+'.\\csv\\csvCleanData\\neutral\\neutral1Data\\'
fileName = "AF3"
fs = 128
xAxis = []

with open(fileDir + fileName + '.csv', 'r+') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter='\r')
    
    for row in csv_reader:
        xAxis.append(int(row[0]))
    
    x = np.array(xAxis)
    f, Pxx_den = signal.periodogram(x, fs, nfft=8)
    """ plt.semilogy(f, Pxx_den)
    plt.show() """
    """ print(f)
    print(Pxx_den) """

    for i in range(0, len(f)):
        print(str(int(f[i])) + ' ' + str(Pxx_den[i]))