# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 14:52:06 2018

@author: Khushbu
"""

import requests
import json

#input - dictSources key= merged trip ids, value = [long1,lat1, long2, lat2]
        #dict destinations dict key= merged trip ids, value = [long1,lat1, long2, lat2]

#output
       # key = merged trips , value = shoretst distance in meters
       
class Conversion:
    
    #def __init__(self,meter):
     #   self.meters = meter
    
    #returns 2 dictionaries - key = merged trip ids, value = shortest distance in meters
    def getShortestPathDetailDict(self,toShortPathSources,toShortPathDest):
        shortPathDataDictSource = dict()
        shortPathDataDictDest = dict()        
        #get shortest path sources:
        for key,value in toShortPathSources.items():
            lonS1=value[0][0]
            latS1=value[0][1]
            lonS2=value[0][2]
            latS2=value[0][3]
            osrmURL = "http://localhost:5000/route/v1/driving/"+str(lonS1) +","+str(latS1)+";"+str(lonS2)+","+str(latS2)+"?overview=false";
            jsonRes = requests.get(osrmURL)
            #load data in a list of dictionaries
            dataDictSource = json.loads(jsonRes.text)
            #structure of this dictionary - dataDict['routes'][0]['distance'], dataDict['routes'][0]['duration'], dataDict['routes'][0]['weight']
            #should I store individual values??
            
            #storing entire dictionary corresponding to trip_ids of merged trips
            #now storing only distance
            shortPathDataDictSource[key] = dataDictSource['routes'][0]['distance']
            
        for key,value in toShortPathDest.items():
            lonD1=value[0][0]
            latD1=value[0][1]
            lonD2=value[0][2]
            latD2=value[0][3]
            osrmURL = "http://localhost:5000/route/v1/driving/"+str(lonD1) +","+str(latD1)+";"+str(lonD2)+","+str(latD2)+"?overview=false";
            jsonRes = requests.get(osrmURL)
            dataDictDest = json.loads(jsonRes.text)
            shortPathDataDictDest[key] = dataDictDest['routes'][0]['distance']
            
        return shortPathDataDictSource,shortPathDataDictDest
    
  
#test
#convObj = Conversion()
#convObj.getShortestPathDetailDict(toShortPathSources,toShortPathDest)