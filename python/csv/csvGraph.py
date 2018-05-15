import matplotlib.pyplot as plt
import numpy as np
import csv
import os

fileDir = os.getcwd()+'\\python\\csv\\clapData\\'
fileName = "AF3"
frequency = 128
xAxis = []
yAxis = []
nbr = 1

with open(fileDir + fileName + '.csv', 'r+') as csvfile:
    plots = csv.reader(csvfile, delimiter='\r')
    
    for row in plots:
        xAxis.append(int(row[0]))
        """ yAxis.append(nbr/frequency)
        nbr += 1 """

    plt.plot(xAxis, label='data from my head !!!')
    plt.show()