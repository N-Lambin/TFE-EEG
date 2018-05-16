import csv
import os
import numpy as np


def csvCleaner(dirName, fileName):
    fileDir = '.\\csv\\csvCleanData\\'
    newDir = fileDir + dirName + '\\' + fileName + 'Data'
    fileNamePath = '.\\csv\\csvRecords\\' + dirName + '\\' + fileName + '.csv'
    nbrOfRow = 0
    if not os.path.exists(newDir):
        os.makedirs(newDir)

        #get information of the file such as date, subject, etc and create other csv files
        with open(fileNamePath, 'r') as csvfile:
            spamreader = csv.reader(csvfile, delimiter = ',')

            for row in spamreader:
                with open(newDir + '/info.txt', 'w+') as info:
                    info.write('\r'.join(row))

                channel = row[5]
                begin = channel.find('AF3')
                end = channel.find('AF4')
                channel = channel[begin: end+3]
                channelList = channel.split(' ')

                for chan in channelList:
                    with open(newDir + '/channelList.txt', 'a+') as channelFileList:
                        channelFileList.write(chan+'\n')
                    channelFile = open(newDir + '/' + chan + '.csv', 'w+')
                    channelFile.close()

                break

            #get information from channels and put it in a different csv file for each channel
            for row in spamreader:
                if nbrOfRow > 5120:
                    for i in range(0, len(channelList)):
                        chan = open(newDir + '/' + channelList[i] + '.csv', 'a')
                        chan.write(str(int(row[i+2].split('.')[0]))+'\n')
                        chan.close()
                nbrOfRow += 1

#def csvToPeriodogram(csvfile) -> np.array:
