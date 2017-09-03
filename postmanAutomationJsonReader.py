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

    def getNameOfEndPointsRequestVerb(self):
        nameOfEndPointRequestVerbList = []
        for item in self.jsonData["item"]:
            nameOfEndPointRequestVerbList.append(item["request"]["method"])
        print ""
        print "Name of endpoint request verb in the JsonFile:"
        print "***********************************"
        for item in nameOfEndPointRequestVerbList:
            print item
        print "***********************************"

    def getNameAndValueOfEndPointRequestHeader(self):
        print ""
        print "Name and value of endpoint request header in the JsonFile:"
        print "***********************************"
        for item in self.jsonData["item"]:
	    for items in item["request"]["header"]:
	 	print items["key"]
		print items["value"]
            print "" 

    def getBodyOfEndpointRequest(self):
        print ""
        print "The Body in the endpoint request from the JsonFile:"
        print "***********************************"
        for item in self.jsonData["item"]:
            body = item["request"]["body"]
            if len(body) > 0:
                print body["mode"]   
                print body["raw"]
                print ""
