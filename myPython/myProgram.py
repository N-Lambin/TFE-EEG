import myLib.myDataExtractor as mde
import glob
import os

csvRecordsFile = '.\\csv\\csvRecords\\'
csvRecordsDirList = glob.glob(csvRecordsFile+'*')

for i in range(0, len(csvRecordsDirList)):
    currentDirName = csvRecordsDirList[i].split('\\')[3]
    csvRecordsFileList = glob.glob(csvRecordsDirList[i]+'\\*.csv')
    for l in range(0, len(csvRecordsFileList)):
        csvFileName = csvRecordsFileList[l].split('\\')[4].split('.')[0]
        mde.csvCleaner(currentDirName, csvFileName)

newFileDir = '.\\csv\\'
newFileName = 'csvMLData'

""" channelList = ['AF3', 'F7', 'F3', 'F4', 'F8', 'AF4']
frequencyList = ['16Hz', '32Hz', '48Hz', '64Hz'] """

csvCleanData = '.\\csv\\csvCleanData\\'
csvCleanDataList = glob.glob(csvCleanData+'*')
    
if os.path.exists(newFileDir + newFileName + '.csv'):
    os.remove(newFileDir + newFileName + '.csv')
    
with open(newFileDir + newFileName + '.csv', 'a+') as csvfile:
    

hope = mde.csvToPeriodogram('neutral', 'neutral1')
print(hope)