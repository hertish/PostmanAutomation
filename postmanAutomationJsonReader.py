import json
from pprint import pprint

class readPostManFile:
    def __init__(self,filePath):
        print 'in self'
        self.filePath = filePath
        self.jsonData = 0 

    def readPostmanCollectionJsonFile(self):
        print 'Reading json file from:',self.filePath
        with open(self.filePath) as data_file:
            self.jsonData = json.load(data_file)
    def getNameOfPostmanCollection(self):
        print "PostmanCollecationName:", self.jsonData["info"]["name"]
