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
            
        return self.sortDistances(combinedDistDict)
    
    def sortDistances(self,combinedDistDict):
        
        sortedList = sorted(combinedDistDict.items(), key=operator.itemgetter(1))
        return sortedList
            
            
        