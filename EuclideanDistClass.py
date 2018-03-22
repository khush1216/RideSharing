# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 14:50:01 2018

@author: Khushbu
"""

import RideDetailsClass


#input - location dictionary
#location dictionary format {"trip_id": <pickup lon, pickup lat, dropoff lon, dropoff lat>}

#output dict - key = merged trip ids , value = [euclidean distance sources]
#        dict-  key = merged trip ids, value = [euclidean distance destination]
#        list - merged trips sent to next pool
#sources dict - key = merged trip ids, value = [long1,lat1,long2,lat2]
#dest    dict - key = merged trip ids, value = [long1,lat1,long2,lat2]
class EuclideanDistance:
    
    def __init__(self,minEuclideanDis):
        self.minEuc = minEuclideanDis
    
    def getEuclideanDistanceDict(self,locationDictioary):
        
        nextPoolIds = set()
        usedPoolIds = set()
        locationDict2 = locationDictioary.copy()
        euclideanDictSources = dict()
        euclideanDictDestinations = dict()
        toShortPathSources = dict()
        toShortPathDest = dict()
        
        #listofLocationList = list()
        for key,value in locationDictioary.items():
            lon1 = value[0]
            lat1 = value[1]
            lon1Dest = value[2]
            lat1Dest = value[3]
            trip_id1 = key
            del locationDict2[key] 
            for key2,value2 in locationDict2.items():
                lon2 = value2[0]
                lat2 = value2[1]
                lon2Dest = value2[2]
                lat2Dest = value2[3]
                trip_id2 = key2
                haversineSource = RideDetailsClass.CalculateHaversine(float(lon1),float(lat1),float(lon2),float(lat2))
                eucDist = haversineSource.haversine()
                haversineDest = RideDetailsClass.CalculateHaversine(float(lon1Dest),float(lat1Dest),float(lon2Dest),float(lat2Dest))
                eucDistDest = haversineDest.haversine()
                
                #################store to db ???
                #check if this is the condition in the algorithm?????????????
                if(eucDist < self.minEuc and eucDistDest < self.minEuc):
                    listCoordSources = list()
                    listCoordDest = list()
                    
                    listCoordSources.append(lon1)
                    listCoordSources.append(lat1)
                    listCoordSources.append(lon2)
                    listCoordSources.append(lat2)
                    
                    listCoordDest.append(lon1Dest)
                    listCoordDest.append(lat1Dest)
                    listCoordDest.append(lon2Dest)
                    listCoordDest.append(lat2Dest)

                    usedPoolIds.add(trip_id1)
                    usedPoolIds.add(trip_id2)
                    eucKey = str(trip_id1) + "," + str(trip_id2) 
                    euclideanDictSources[eucKey] = eucDist
                    euclideanDictDestinations[eucKey] = eucDistDest
                    
                    toShortPathSources[eucKey] = listCoordSources
                    toShortPathDest[eucKey] = listCoordDest
               
                #send the trips to the next pool
                else:
                    if(not trip_id1 in usedPoolIds):
                        nextPoolIds.add(trip_id1)
                    if(not trip_id2 in usedPoolIds):
                        nextPoolIds.add(trip_id2)
                                    
        #print (len(euclideanDict))
        return euclideanDictSources,euclideanDictDestinations,nextPoolIds,toShortPathSources,toShortPathDest
 
#test
#euclObj = EuclideanDistance(2)
#eucDistS, eucDistDest, nextPoolID,toShortPathSources, toShortPathDest = euclObj.getEuclideanDistanceDict(loc)

#toShortPathSources
#toShortPathDest
