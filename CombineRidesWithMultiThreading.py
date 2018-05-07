from threading import Thread
from queue import Queue
import json
import time
import urllib3
#import requests


#input - dictSources key= merged trip ids, value = [long1,lat1, long2, lat2]
        #dict destinations dict key= merged trip ids, value = [long1,lat1, long2, lat2]

#output
       # key = merged trips , value = shoretst distance in meters
       
class Conversion:
    
    conn_pool = urllib3.PoolManager()
    #conn_pool = requests.Session()
    qres = Queue()
    concurrent = 100
    q = Queue(concurrent)
    
    
    #returns 2 dictionaries - key = merged trip ids, value = shortest distance in meters
    def getShortestPathDetailDict(self,toShortPathSources,toShortPathDest):
        shortPathDataDictSource = dict()
        shortPathDataDictDest = dict()        
        #get shortest path sources:
        tic = time.clock()
        
        #temp = list(toShortPathSources.items());
        #print("Key: ",temp[0][0], "lonS1: ", temp[0][1][0][0], "lats1: ", temp[0][1][0][1], "lons2: ", temp[0][1][0][2], "lats2: ",temp[0][1][0][3])
        #conn_pool = urllib3.HTTPConnectionPool(host="http://localhost/", port="5000", maxsize=1)
        sourceList = dict()
        for key,value in toShortPathSources.items():
            lonS1=value[0][0]
            latS1=value[0][1]
            lonS2=value[0][2]
            latS2=value[0][3]
            osrmURL = "http://localhost:5000/route/v1/driving/"+str(lonS1) +","+str(latS1)+";"+str(lonS2)+","+str(latS2)+"?overview=false";
            sourceList[key] = osrmURL
        
        a = time.clock()
        for i in range(self.concurrent):
            t = Thread(target=self.doWork)
            t.daemon = True
            t.start()
        for key,url in sourceList.items():
            self.q.put([url,key])
        self.q.join()
        b = time.clock()
        print("First loop   :    ", b-a, "  Size  :  ", len(sourceList))
        for x in range(self.qres.qsize()):
            shortPathDataDictSource.update(self.qres.get())
            
        destList = dict()
        for key,value in toShortPathDest.items():
            lonD1=value[0][0]
            latD1=value[0][1]
            lonD2=value[0][2]
            latD2=value[0][3]
            osrmURL = "http://localhost:5000/route/v1/driving/"+str(lonD1) +","+str(latD1)+";"+str(lonD2)+","+str(latD2)+"?overview=false";
            destList[key]=osrmURL
        
        for i in range(self.concurrent):
            t = Thread(target=self.doWork)
            t.daemon = True
            t.start()
        for key,url in destList.items():
            self.q.put([url,key])
        self.q.join()
        
        for x in range(self.qres.qsize()):
            shortPathDataDictDest.update(self.qres.get())
        
        toc = time.clock()
        print (toc-tic)
        print ("LALALALALA")
        # Get results
        #calc_routes = [qres.get() for _ in range(len(url_routes))]
        return shortPathDataDictSource,shortPathDataDictDest
    
    def doWork(self):
        while True:
            url,key = self.q.get()
            resp = self.getReq(url)
            #print(resp)
            self.processReq(resp, key)
            self.q.task_done()
    
    def getReq(self, url):
        #try:
            resp = self.conn_pool.request('GET', url)
            #resp = self.conn_pool.get(url)
            #print(resp.content)
            return resp
        #except:
            #return 999, None
        
    def processReq(self, resp, key):
        #try:
            #dataDictSource = json.loads(resp.data.decode('utf-8'))
            #print(resp)
            dataDictSource = json.loads(resp.data.decode('utf-8'))
            #dataDictSource = json.loads(resp.text)
            tot_dist_m = dataDictSource['routes'][0]['distance']
            out = dict()
            out[key] = tot_dist_m
        #except Exception as err:
            #print("Error: ", err, key)
            #out = dict()
            #out[key] = 0
            self.qres.put(out)
            return