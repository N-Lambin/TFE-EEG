import myLib.mySSH as ssh
import myLib.mySupervisedLearning as msl
import myLib.myDataExtractor as mde
import myLib.myCommand as mco
import glob
import os

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

channelList = ['AF3', 'F3', 'F4', 'F8', 'AF4']
frequencyList = ['2Hz', '4Hz']

csvCleanData = '.\\csv\\csvCleanData\\'
csvCleanDataDirList = glob.glob(csvCleanData + '*')
    
if os.path.exists(newFileDir + newFileName + '.csv'):
    os.remove(newFileDir + newFileName + '.csv')
    
with open(newFileDir + newFileName + '.csv', 'a+') as csvfile:
    for i in range(0, len(csvCleanDataDirList)):
        currentDirName1 = csvCleanDataDirList[i].split('\\')[3]
        csvCleanDataDirDirList = glob.glob(csvCleanData + currentDirName1 + '\\*')
        for l in range(0, len(csvCleanDataDirDirList)):
            currentDirName2 = csvCleanDataDirDirList[l].split('\\')[4].split('Data')[0]
            csvfile.write(mde.csvToPeriodogram(currentDirName1, currentDirName2, channelList, 64))

#train the supervised learning algorithm
model = msl.trainingDecisionTree()

#exemple of prediction
""" data = [[37.6695, 5.56588, 6.60943, 9.56798, 20.6567, 5.13102, 1.44630, 0.43651, 0.04982, 0.15489]]
command = model.predict(data) """

#get the token for the API connection
token = mco.getToken()