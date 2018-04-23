# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 22:43:59 2018

@author: singh
"""
import CombineRides
import requests
import json
import operator
class DistSaved:
    
    
    def diffSavedDistance(self, mergeableSource, mergeableDest,originalDist):
        distanceTravelled = self.distOf4Comb(mergeableSource,mergeableDest)
        distSavedDict = dict()
        
        for key,value in distanceTravelled.items():
            trip1,trip2 = key.split(",")
            
            origTotaltrip1trip2 = originalDist[int(trip1)] + originalDist[int(trip2)]
                
            tripDiff = origTotaltrip1trip2 - (value[1] * 0.000621371)
            #print (key + " " + str(origTotaltrip1trip2) + " " + str(value[1]))
            
            distSavedDict[key] = tripDiff
            
        return distSavedDict

    
    def distOf4Comb(self,mergeableSource,mergeableDest):
        distTravelled = dict()
        #convertToListObj = CombineRides.CombineRides()
        #listMergeableRide = convertToListObj.convertToList(mergeableRides)
        
        #print(listMergeableRide)
        for key,value in mergeableSource.items():
            trip1,trip2 = key.split(",")
            keyRoute = "routes"
            lonS1=value[0][0]
            latS1=value[0][1]
            lonS2=value[0][2]
            latS2=value[0][3]
            valueDest = mergeableDest.get(key)
            lonD1=valueDest[0][0]
            latD1=valueDest[0][1]
            lonD2=valueDest[0][2]
            latD2=valueDest[0][3]
            orderDistDict = dict()
            #*********************1st order s1 s2 d1 d2************************************
            
            osrmURL = "http://localhost:5000/route/v1/driving/"+str(lonS1) +","+str(latS1)+";"+str(lonS2)+","+str(latS2)+";"+str(lonD1) +","+str(latD1)+";"+str(lonD2)+","+str(latD2)+"?overview=false";
            print (osrmURL)
            print (trip1)
            print(trip2)

            jsonRes = requests.get(osrmURL)
            #load data in a list of dictionaries
            dataDictSource = json.loads(jsonRes.text)
            rideOrderKey = str(trip1)+","+str(trip2)+","+str(trip1)+","+str(trip2)
            #structure of this dictionary - dataDict['routes'][0]['distance'], dataDict['routes'][0]['duration'], dataDict['routes'][0]['weight']
            #should I store individual values??
            
            #storing entire dictionary corresponding to trip_ids of merged trips
            #now storing only distance
            if (keyRoute not in dataDictSource.keys()):
                print('route not present')
            else:
                orderDistDict[rideOrderKey] = dataDictSource['routes'][0]['distance']
                print (orderDistDict) 
                
            
            #********************** 2nd order s2 s1 d1 d2***********************************
            osrmURL = "http://localhost:5000/route/v1/driving/"+str(lonS2) +","+str(latS2)+";"+str(lonS1)+","+str(latS1)+";"+str(lonD1) +","+str(latD1)+";"+str(lonD2)+","+str(latD2)+"?overview=false";
            jsonRes = requests.get(osrmURL)
            #load data in a list of dictionaries
            dataDictSource = json.loads(jsonRes.text)
            rideOrderKey = str(trip2)+","+str(trip1)+","+str(trip1)+","+str(trip2)
            #structure of this dictionary - dataDict['routes'][0]['distance'], dataDict['routes'][0]['duration'], dataDict['routes'][0]['weight']
            #should I store individual values??
            
            #storing entire dictionary corresponding to trip_ids of merged trips
            #now storing only distance
            if (keyRoute not in dataDictSource.keys()):
                print('route not present')
            else:
                orderDistDict[rideOrderKey] = dataDictSource['routes'][0]['distance']
                
            #********************** 3rd order s1 s2 d2 d1***********************************
            osrmURL = "http://localhost:5000/route/v1/driving/"+str(lonS1) +","+str(latS1)+";"+str(lonS2)+","+str(latS2)+";"+str(lonD2) +","+str(latD2)+";"+str(lonD1)+","+str(latD1)+"?overview=false";
            jsonRes = requests.get(osrmURL)
            #load data in a list of dictionaries
            dataDictSource = json.loads(jsonRes.text)
            rideOrderKey = str(trip1)+","+str(trip2)+","+str(trip2)+","+str(trip1)
            #structure of this dictionary - dataDict['routes'][0]['distance'], dataDict['routes'][0]['duration'], dataDict['routes'][0]['weight']
            #should I store individual values??
            
            #storing entire dictionary corresponding to trip_ids of merged trips
            #now storing only distance
            
            if (keyRoute not in dataDictSource.keys()):
                print('route not present')
            else:
                orderDistDict[rideOrderKey] = dataDictSource['routes'][0]['distance']
            
            #********************** 4th order s2 s1 d2 d1***********************************
            osrmURL = "http://localhost:5000/route/v1/driving/"+str(lonS2) +","+str(latS2)+";"+str(lonS1)+","+str(latS1)+";"+str(lonD2) +","+str(latD2)+";"+str(lonD1)+","+str(latD1)+"?overview=false";
            jsonRes = requests.get(osrmURL)
            #load data in a list of dictionaries
            dataDictSource = json.loads(jsonRes.text)
            rideOrderKey = str(trip2)+","+str(trip1)+","+str(trip2)+","+str(trip1)
            #structure of this dictionary - dataDict['routes'][0]['distance'], dataDict['routes'][0]['duration'], dataDict['routes'][0]['weight']
            #should I store individual values??
            
            #storing entire dictionary corresponding to trip_ids of merged trips
            #now storing only distance
            if (keyRoute not in dataDictSource.keys()):
                print('route not present')
            else:
                orderDistDict[rideOrderKey] = dataDictSource['routes'][0]['distance']
            
            #finding min dist combination
            if (orderDistDict):
                minDistRide = min(orderDistDict.items(), key=operator.itemgetter(1))
                valueList = list()
                valueList.append(minDistRide[0])
                valueList.append(minDistRide[1])
                distTravelled[key] = valueList
        return distTravelled
    
    
    
        
        
        
        
        
        