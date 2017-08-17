import json

class readPostManFile:
    def __init__(self,filePath):
        self.filePath = filePath
        self.jsonData = 0 

    def readPostmanCollectionJsonFile(self):
        print 'Reading json file from:',self.filePath
        with open(self.filePath) as data_file:
            self.jsonData = json.load(data_file)
    def getNameOfPostmanCollection(self):
        print "PostmanCollecationName:", self.jsonData["info"]["name"]
    def getNameOfEndPoints(self):
        nameOfEndPointList = []
        for item in self.jsonData["item"]:
            nameOfEndPointList.append(item["name"])
        print ""
        print "Name of endpoints in the JsonFile:"
        print "***********************************"
        for item in nameOfEndPointList:
            print item
        print "***********************************"
    def getNameOfEndPointsRequestURL(self):
        nameOfEndPointRequestURLList = []
        for item in self.jsonData["item"]:
            nameOfEndPointRequestURLList.append(item["request"]["url"])
        print ""
        print "Name of endpoint request URL in the JsonFile:"
        print "***********************************"
        for item in nameOfEndPointRequestURLList:
            print item
        print "***********************************"
