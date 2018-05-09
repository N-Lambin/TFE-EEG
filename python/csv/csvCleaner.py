import csv
import os

fileDir = os.getcwd()+'\\csv\\'
fileName = "clap2"


#create directory
newDir = fileDir + fileName + 'DataCQ'
if not os.path.exists(newDir):
    os.makedirs(newDir)

    #get information of the file such as date, subject, etc and create csv file
    with open(fileDir + fileName + '.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter = ',')

        for row in spamreader:
            info = open(newDir + '/info.txt', 'w+')
            info.write('\r'.join(row))
            info.close()

            channel = row[5]
            begin = channel.find('AF3')
            end = channel.find('AF4')

            channel = channel[begin: end+3]

            chanList = channel.split(' ')
            for chan in chanList:
                chan = open(newDir + '/' + chan + '.csv', 'w+')
                chan.close()

            break

        #get information from channels and put it in a different csv file for each channel
        for row in spamreader:
            for i in range(0, len(chanList)):
                chan = open(newDir + '/' + chanList[i] + '.csv', 'a')
                chan.write(str(int(row[i+2].split('.')[0]))+'\n')
                chan.close()