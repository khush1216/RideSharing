# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 12:02:55 2018

@author: Khushbu
"""

import operator

class CombineRides:
    
    
    def mergeSourceDestDist(self, sourceMap, destMap):
        combinedDistDict = dict()
        for key,sourceDist in sourceMap.items():
            
            destDist = destMap[key]
            combinedDistDict[key] = destDist + sourceDist
            
        #print (combinedDistDict)
        return self.sortDistances(combinedDistDict)
    
    def sortDistances(self,combinedDistDict):
        
        sortedList = sorted(combinedDistDict.items(), key=operator.itemgetter(1))
        return sortedList
    
    def convertToList(self,DistTripTuples):
        finalDistTripList = list()
        addedDist = list(DistTripTuples.values())
        for x in range(0,len(DistTripTuples)-1):
            miniMergedList = list()
            convertKeysToList= list(DistTripTuples.keys())
            trip1,trip2 = (convertKeysToList[x]).split(",")
            miniMergedList.append(int(trip1))
            miniMergedList.append(int(trip2))
            temp = float(addedDist[x])
            miniMergedList.append(temp)
            finalDistTripList.append(miniMergedList)
            
        return finalDistTripList
    """def convertToList(self,sortedTripTuples):
        finalMergedTripList = list()
        for x in range(0,len(sortedTripTuples)-1):
            miniMergedList = list()
            trip1,trip2 = (sortedTripTuples[x][0]).split(",")
            miniMergedList.append(int(trip1))
            miniMergedList.append(int(trip2))
            finalMergedTripList.append(miniMergedList)
            
        print (finalMergedTripList)"""
    
    """def finalMergedRides(self, finalMergedTripList):
        
        mergedRidesList = list()
        copyfinalMergedTripList = finalMergedTripList[:]
        
        for miniMergedList in finalMergedTripList:
            mergedRidesList.append(miniMergedList)
            trip1 = miniMergedList[0]
            trip2 = miniMergedList[1]
            copyfinalMergedTripList.remove(miniMergedList)
            
            for nextMiniMergedList in copyfinalMergedTripList:
                if trip1 in nextMiniMergedList or trip """
            
            
            
            
            
            
            
            
            
            
        