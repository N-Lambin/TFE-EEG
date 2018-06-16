import matplotlib.pyplot as plt
import csv
import numpy as np
from scipy import signal

fileDir = 'winkLeft\\winkLeft10Data\\'
fileName = 'AF3.csv'
fs = 128
x = []

with open(".\\csv\\csvCleanData\\" + fileDir + fileName, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = '\r')

    for row in csv_reader:
        x.append(int(row[0]))

    x = np.array(x)
    f, fd = signal.periodogram(x, fs, nfft=64)
    plt.semilogy(f, fd, 'r')

fileDir = 'neutral\\neutral10Data\\'
fileName = 'AF3.csv'
fs = 128
x = []

with open(".\\csv\\csvCleanData\\" + fileDir + fileName, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = '\r')

    for row in csv_reader:
        x.append(int(row[0]))

    x = np.array(x)
    f, fd = signal.periodogram(x, fs, nfft=64)
    plt.semilogy(f, fd, 'b')
    plt.show()