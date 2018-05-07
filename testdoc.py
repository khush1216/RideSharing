# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 14:53:18 2018

@author: Khushbu
"""
import dbConnection
import RideDetailsClass
import EuclideanDistClass
import ConversionShortPath
import CombineRides
import itertools
import DistSaved

import maxMatching



#testing block
dbConnObj = dbConnection.DB_Connect()
rideDetails = RideDetailsClass.RideDetailClass()
con = dbConnObj.dbConnection()

skippedRecordOffset = 0;
while (skippedRecordOffset != 9725912):
    loc, fare, passCount, drop, offs, originalDistDict = rideDetails.getRideDetails(con,str(skippedRecordOffset))
    skippedRecordOffset = skippedRecordOffset + offs
    
    print (skippedRecordOffset)
    euclObj = EuclideanDistClass.EuclideanDistance(2)
    eucDistS, eucDistDest, nextPoolID,toShortPathSources, toShortPathDest, individualTrips = euclObj.getEuclideanDistanceDict(loc,passCount)

    #print (toShortPathSources['107,145'])
    #print (toShortPathDest['107,145'])


    d1TestSource = dict(itertools.islice(iter(toShortPathSources.items()),100))
    d1TestDest = dict(itertools.islice(iter(toShortPathDest.items()),100))

    #print (originalDistDict)
    #print (d1TestSource)
    #print (d1TestDest)

    distSavedObj = DistSaved.DistSaved()
    newListDistSaved = distSavedObj.diffSavedDistance(d1TestSource,d1TestDest,originalDistDict)
    
    convertToListObj = CombineRides.CombineRides()
    savedDistoList = convertToListObj.convertToList(newListDistSaved)

    maxMatchingObj= maxMatching.MaxMatching()
    mergedRides = maxMatchingObj.getMergedRides(savedDistoList)

    mergedRidesWithSavedDist = maxMatchingObj.getMergedRidesWithSavedDist(mergedRides,newListDistSaved)
    print (mergedRidesWithSavedDist)
            
            

#    print (mergedRides)



#convObj = ConversionShortPath.Conversion()
#sourceDetails,destDetails = convObj.getShortestPathDetailDict(d1TestSource,d1TestDest)

#combineObj = CombineRides.CombineRides()
#sortedMap = combineObj.mergeSourceDestDist(sourceDetails,destDetails)

#print (sortedMap)
#combineObj.convertToList(sortedMap)
#print (sourceDetails['1,7'])
#print (destDetails['1,7'])"""
