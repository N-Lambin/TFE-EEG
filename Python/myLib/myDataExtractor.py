import csv
import os
import numpy as np
from scipy import signal
from sklearn.decomposition import FastICA

def infoToTxt(newFileDir, row):
    with open(newFileDir + '/info.txt', 'w+') as info:
        info.write('\r'.join(row))

        channel = row[5]
        begin = channel.find('AF3')
        end = channel.find('AF4')
        channel = channel[begin: end+3]
        channelList = channel.split(' ')

        for chan in channelList:
            with open(newFileDir + '/channelList.txt', 'a+') as channelFileList:
                channelFileList.write(chan+'\n')
            channelFile = open(newFileDir + '/' + chan + '.csv', 'w+')
            channelFile.close()
        return channelList

def csvCleaner(dirName, fileName):
    newFileDir = '.\\csv\\csvCleanData\\' + dirName + '\\' + fileName + 'Data'
    csvFilePath = '.\\csv\\csvRecords\\' + dirName + '\\' + fileName + '.csv'
    nbrOfRow = 0
    if not os.path.exists(newFileDir):
        os.makedirs(newFileDir)

        #get information of the file such as date, subject, etc and create other csv files
        with open(csvFilePath, 'r') as csvfile:
            spamreader = csv.reader(csvfile, delimiter = ',')

            for row in spamreader:
                channelList = infoToTxt(newFileDir, row)
                break

            #get information from channels and put it in a different csv file for each channel
            for row in spamreader:
                if nbrOfRow > 1280:
                    for i in range(0, len(channelList)):
                        chan = open(newFileDir + '/' + channelList[i] + '.csv', 'a')
                        chan.write(str(int(row[i+2].split('.')[0]))+'\n')
                        chan.close()
                nbrOfRow += 1

def csvToPSA(dirName, fileName, channelList, nfft, fs):
    signal1 = openFile(dirName, fileName, channelList[0])
    signal2 = openFile(dirName, fileName, channelList[1])
    signal3 = openFile(dirName, fileName, channelList[2])
    signal4 = openFile(dirName, fileName, channelList[3])
    signal5 = openFile(dirName, fileName, channelList[4])
    signal6 = openFile(dirName, fileName, channelList[5])
    signal7 = openFile(dirName, fileName, channelList[6])
    signal8 = openFile(dirName, fileName, channelList[7])
    signal9 = openFile(dirName, fileName, channelList[8])
    signal10 = openFile(dirName, fileName, channelList[9])

    dataSourceArray = np.c_[fastICA(signal1, signal2, signal3, signal4, signal5), \
        fastICA(signal6, signal7, signal8, signal9, signal10)]
    strData = ''

    for i in range(0, 6):
        dataSource = dataSourceArray[i,:]
        frequencySampleList, powerSpectralArray = signal.periodogram(dataSource, fs=fs, nfft=nfft)

        for l in range(1,5,2):
            strData += "{0:.7}".format(str(powerSpectralArray[l])) + ','

    strData += dirName + '\n'
    return strData

def openFile(dirName, fileName, captor):
    filePath = '.\\csv\\csvCleanData\\' + dirName + '\\' + fileName + 'Data\\'
    dataSource = []

    if os.path.exists(filePath):
        with open(filePath + captor + '.csv', 'r') as csvfile:
            spamreader = csv.reader(csvfile, delimiter='\r')

            for row in spamreader:
                dataSource.append(int(row[0]))
            dataSource = np.array(dataSource)

            return dataSource

def fastICA(signal1, signal2, signal3, signal4, signal5):
    signalsArray = np.c_[signal1, signal2, signal3, signal4, signal5]
    ica = FastICA(n_components=3, max_iter=5000, tol=0.5)
    S_ = np.array(ica.fit_transform(signalsArray))

    return S_