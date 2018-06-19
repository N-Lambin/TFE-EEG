import myLib.mySSH as ssh
import myLib.mySupervisedLearning as msl
import myLib.myDataExtractor as mde
import myLib.myCommand as mco

import glob
import os

import numpy as np
import pandas
import os
from sklearn import decomposition

#extract data from csv file
csvRecordsFile = '.\\csv\\csvRecords\\'
csvRecordsDirList = glob.glob(csvRecordsFile + '*')

for i in range(0, len(csvRecordsDirList)):
    currentDirName = csvRecordsDirList[i].split('\\')[3]
    csvRecordsFileList = glob.glob(csvRecordsDirList[i]+'\\*.csv')
    for l in range(0, len(csvRecordsFileList)):
        csvFileName = csvRecordsFileList[l].split('\\')[4].split('.')[0]
        mde.csvCleaner(currentDirName, csvFileName)

newFileDir = '.\\csv\\'
newFileName = 'csvMLData'

channelList = ['AF3', 'F7', 'F3', 'F4', 'F8', 'AF4']
frequencyList = ['2Hz', '4Hz']

csvCleanData = '.\\csv\\csvCleanData\\'
csvCleanDataDirList = glob.glob(csvCleanData + '*')
    
if not os.path.exists(newFileDir + newFileName + '.csv'):
    #os.remove(newFileDir + newFileName + '.csv')
    
    with open(newFileDir + newFileName + '.csv', 'a+') as csvfile:
        for i in range(0, len(csvCleanDataDirList)):
            currentDirName1 = csvCleanDataDirList[i].split('\\')[3]
            csvCleanDataDirDirList = glob.glob(csvCleanData + currentDirName1 + '\\*')
            for l in range(0, len(csvCleanDataDirDirList)):
                currentDirName2 = csvCleanDataDirDirList[l].split('\\')[4].split('Data')[0]
                csvfile.write(mde.csvToPSA(currentDirName1, currentDirName2, channelList, 256, 64))

names = ['ICA1', 'ICA1bis', 'ICA1bis2', 'ICA2', 'ICA2bis','ICA2bis2', 'ICA3', 'ICA3bis', 'ICA3bis2','ICA4', 'ICA4bis', 'ICA4bis2', 'class']
#names = ['ICA1', 'ICA1bis', 'ICA2', 'ICA2bis', 'ICA3', 'ICA3bis','ICA4', 'ICA4bis', 'class']
dataset = pandas.read_csv('.\\csv\\csvMLData.csv', names=names)

array = dataset.values
X = array[:,0:12]
Y = array[:,12]

n_components=4

pca = decomposition.PCA(n_components=n_components)
pca.fit(X)
X = pca.transform(X)

if not os.path.exists('.\\csv\\pcaData.csv'):
    #os.remove('.\\csv\\pcaData.csv')

    with open('.\\csv\\pcaData.csv', 'a+') as csvfile:
        for i in range(0, len(X)):
            info = ''
            for ii in range(0, n_components):
                value = X[i][ii]
                info += "{0:.7}".format(str(value)) + ','
            info+= Y[i] + '\n'
            csvfile.write(info)

#train the supervised learning algorithm
model = msl.trainingDecisionTree()