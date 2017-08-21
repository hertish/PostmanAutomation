import postmanAutomationJsonReader
import ConfigParser
import sys

#read operative system
osSystem = sys.platform

#Read the ini file for config parameters
config = ConfigParser.ConfigParser()
config.readfp(open(r'postmanAutomation.ini'))
if osSystem == "darwin":
    filePath = config.get('Variables and Paths', 'filePathMac')
else:
    filePath = config.get('Variables and Paths', 'filePathWin') 

print 'Starting postman automation in OS system ', osSystem

#Create an instance of readPostman class
ref_to_readPostmanFile = postmanAutomationJsonReader.readPostManFile(filePath)

#Read jsonFile
ref_to_readPostmanFile.readPostmanCollectionJsonFile()
#Get name of postmanCollection
ref_to_readPostmanFile.getNameOfPostmanCollection()
#Get names of endpoints
ref_to_readPostmanFile.getNameOfEndPoints()
#Get names of endpoints requests url
ref_to_readPostmanFile.getNameOfEndPointsRequestURL()
#Get names of endpoints requests verb
ref_to_readPostmanFile.getNameOfEndPointsRequestVerb()
#Get name and value of endpoints requests header 
ref_to_readPostmanFile.getNameAndValueOfEndPointRequestHeader()
