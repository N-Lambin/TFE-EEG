import myLib.myDataExtractor as mde
import glob

csvRecordsFile = '.\\csv\\csvRecords\\'
csvRecordsDirList = glob.glob(csvRecordsFile+'*')

for i in range(0, len(csvRecordsDirList)):
    currentDirName = csvRecordsDirList[i].split('\\')[3]
    csvRecordsFileList = glob.glob(csvRecordsDirList[i]+'\\*.csv')
    for l in range(0, len(csvRecordsFileList)):
        csvFileName = csvRecordsFileList[l].split('\\')[4].split('.')[0]
        mde.csvCleaner(currentDirName, csvFileName)

""" newFileDir = '.\\csv\\'
    newFileName = 'csvMLData'
    
    if os.path.exists(newFileDir + newFileName + '.csv'):
        os.remove(newFileDir + newFileName + '.csv')
    
    with open(newFileDir + newFileName + '.csv', 'a+') as csvfile: """

hope = mde.csvToPeriodogram('neutral', 'neutral1')
print(hope)