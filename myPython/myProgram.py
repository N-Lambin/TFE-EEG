import myLib.myDataExtractor as mde
import glob

csvRecordsFile = '.\\csv\\csvRecords\\'
csvRecordsDirList = glob.glob(csvRecordsFile+'*')

for i in range(0, len(csvRecordsDirList)):
    currentDirName = csvRecordsDirList[i].split('\\')[3]
    csvRecordsFileList = glob.glob(csvRecordsDirList[i]+'\\*.csv')
    #if len(csvRecordsFileList) != 0:
    for l in range(0, len(csvRecordsFileList)):
        print(csvRecordsFileList[l].split('\\')[4].split('.')[0])

#mde.csvCleaner('neutral', 'neutral1')