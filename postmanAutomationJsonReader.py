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
        postmanAutomationLogger.PostManLogger("info", "Name of endpoints in the JsonFile:").postManAutomationLogging()
        postmanAutomationLogger.PostManLogger("info","******************************************************************").postManAutomationLogging()
        for item in nameOfEndPointList:
            postmanAutomationLogger.PostManLogger("info","EndPoint:",item).postManAutomationLogging()
        postmanAutomationLogger.PostManLogger("info", "******************************************************************").postManAutomationLogging()

    def getNameOfEndPointsRequestURL(self):
        nameOfEndPointRequestURLList = []
        for item in self.jsonData["item"]:
            nameOfEndPointRequestURLList.append(item["request"]["url"])
        postmanAutomationLogger.PostManLogger("info","Name of endpoint request URL in the JsonFile:").postManAutomationLogging()
        postmanAutomationLogger.PostManLogger("info", "******************************************************************").postManAutomationLogging()
        for item in nameOfEndPointRequestURLList:
            postmanAutomationLogger.PostManLogger("info","Request URL:",item).postManAutomationLogging()
        postmanAutomationLogger.PostManLogger("info", "******************************************************************").postManAutomationLogging()

    def getNameOfEndPointsRequestVerb(self):
        nameOfEndPointRequestVerbList = []
        for item in self.jsonData["item"]:
            nameOfEndPointRequestVerbList.append(item["request"]["method"])
        postmanAutomationLogger.PostManLogger("info","Name of endpoint request verb in the JsonFile:").postManAutomationLogging()
        postmanAutomationLogger.PostManLogger("info","******************************************************************").postManAutomationLogging()
        for item in nameOfEndPointRequestVerbList:
            postmanAutomationLogger.PostManLogger("info","Verb:",item).postManAutomationLogging()
        postmanAutomationLogger.PostManLogger("info","******************************************************************").postManAutomationLogging()

    def getNameAndValueOfEndPointRequestHeader(self):
        postmanAutomationLogger.PostManLogger("info","Name and value of endpoint request header in the JsonFile:").postManAutomationLogging()
        postmanAutomationLogger.PostManLogger("info","******************************************************************").postManAutomationLogging()
        for item in self.jsonData["item"]:
            for items in item["request"]["header"]:
                postmanAutomationLogger.PostManLogger("info","Key:",items["key"]).postManAutomationLogging()
                postmanAutomationLogger.PostManLogger("info","Value:",items["value"]).postManAutomationLogging()
                postmanAutomationLogger.PostManLogger("info","**************************").postManAutomationLogging()

    def getBodyOfEndpointRequest(self):
        postmanAutomationLogger.PostManLogger("info","The body in the endpoint request from the JsonFile:").postManAutomationLogging()
        postmanAutomationLogger.PostManLogger("info","******************************************************************").postManAutomationLogging()
        for item in self.jsonData["item"]:
            body = item["request"]["body"]
            if len(body) > 0:
                postmanAutomationLogger.PostManLogger("info", "**************************").postManAutomationLogging()
                postmanAutomationLogger.PostManLogger("info","mode:",body["mode"]).postManAutomationLogging()
                postmanAutomationLogger.PostManLogger("info","raw:", body["raw"]).postManAutomationLogging()
        postmanAutomationLogger.PostManLogger("info","******************************************************************").postManAutomationLogging()
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

