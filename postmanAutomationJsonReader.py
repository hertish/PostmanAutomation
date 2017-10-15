import json
import postmanAutomationLogger

class readPostManFile:
    def __init__(self,filePath):
        self.filePath = filePath
        self.jsonData = 0 

    def readPostmanCollectionJsonFile(self):
        postmanAutomationLogger.PostManLogger("info", "Reading json file from:",self.filePath).postManAutomationLogging()
        with open(self.filePath) as data_file:
            self.jsonData = json.load(data_file)

    def getNameOfPostmanCollection(self):
        postmanAutomationLogger.PostManLogger("info", "PostManCollectionName:",self.jsonData["info"]["name"]).postManAutomationLogging()

    def getNameOfEndPoints(self):
        nameOfEndPointList = []
        for item in self.jsonData["item"]:
            nameOfEndPointList.append(item["name"])
        print ""
        postmanAutomationLogger.PostManLogger("info", "Name of endpoints in the JsonFile:").postManAutomationLogging()
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

        print 'THE DICT'
        #verb = "PUT"
        #d =  {}
        #d['name'] = "martin"
        #d['url'] = "http:www.hotmail.com"
        #d['raw'] = "vpn:mullvad.net"
        #for i in d:
        #    if i == 'raw':
        #        print i, d[i]
        endpointName = "getToken"
        urlRequest = "www.aftonbladet.se"
        verb = "GET"
        header = "accetString"
        body = "name=martin"
        endpointName1 = "getBajs"
        urlRequest1 = "www.gp.se"
        verb1 = "POST"
        header1 = "accetString"
        body1 = "name=martina"
        
        jSonReaderDataList = []
        jSonReaderDataList.append(dict(EndPointName=endpointName,UrlRequest=urlRequest,Verb='null',Header=header,Body=body))
        jSonReaderDataList.append(dict(EndPointName=endpointName1,UrlRequest=urlRequest1,Verb='null',Header=header1,Body=body1))
        for i, request in enumerate(jSonReaderDataList):
            #print "hej"
            #print i
            #print requests
            #plocka ut ur dicten:
            print jSonReaderDataList[i]['EndPointName']
            #insert in dicten
            request['Verb'] = "pussssyyyy"
            print '' 
        print jSonReaderDataList

