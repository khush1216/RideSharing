# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 14:49:07 2018

@author: Khushbu
"""

from math import radians, cos, sin, asin, sqrt

#input - connection object, no. of skipped records
#output - locationDict - key = trip_ids, value = [longPickup, latPickup, longDropoff, latDropoff]
        #- fareAmountDict - key=[trip_ids] value = [trip amount]
        #dropff time dict = key = [trip_ids], value = [drop off time]
        #new -offset - no.of records to be skipped to get the next pool so that there's no need to iterate through those again

#example query
#select * from neworiginal_data where tpep_pickup_datetime > '2016-01-01 00:00:06' order by tpep_pickup_datetime limit 10;
class RideDetailClass:     
    #time window of 5 minutes
    
    def getFirstRecordPickupTimeStamp(self,connObj,skippedRecords):
       query = "SELECT tpep_pickup_datetime FROM neworiginal_data limit " + skippedRecords + ", 1";
       cursor = connObj.cursor();
       cursor.execute(query);
       record = cursor.fetchone()
       return record[0]
        
    def getRideDetails(self, connObj,skippedRecOffset):
        
        locationDict = dict() #pickup and dropoffs
        fareAmountDict = dict()
        dropoffTimeDict = dict()
        passengerCount = dict()
        starttime = self.getFirstRecordPickupTimeStamp(connObj,skippedRecOffset).strftime("%Y-%m-%d %H:%M:%S")
        query = "select * from neworiginal_data where TIMESTAMPDIFF(MINUTE," + "'" + starttime + "'" + ", tpep_pickup_datetime) < 2 order by tpep_pickup_datetime limit " + skippedRecOffset + "," + "11111111111111111111;"
        
        #queryCount = "select count(*) from neworiginal_data where TIMESTAMPDIFF(MINUTE," + "'" + starttime + "'" + ", tpep_pickup_datetime) < 1 order by tpep_pickup_datetime limit " + skippedRecOffset + "," + "11111111111111111111;"        
        #remove the retrieved data?
        cursor = connObj.cursor();
        cursor.execute(query);
        new_offset = 0 #no. of skipped records in the next iteration
        for row in cursor:
            location = list()
            location.append(row[5])
            location.append(row[6])
            location.append(row[8])
            location.append(row[9])

            locationDict[row[13]] = location
            fareAmountDict[row[13]] = row[12]
            dropoffTimeDict[row[13]] = row[2]
            passengerCount[row[13]] = row[3]
            new_offset = new_offset+1
        
        
        return locationDict,fareAmountDict, passengerCount,dropoffTimeDict,new_offset
    
class CalculateHaversine:
    
    def __init__(self,lon1,lat1,lon2,lat2):
        self.lon1 = lon1
        self.lat1 = lat1
        self.lon2 = lon2
        self.lat2 = lat2


    def haversine(self):
    
        # convert decimal degrees to radians 
        self.lon1, self.lat1, self.lon2, self.lat2 = map(radians, [self.lon1, self.lat1, self.lon2, self.lat2])

        # haversine formula 
        dlon = self.lon2 - self.lon1 
        dlat = self.lat2 - self.lat1 
        a = sin(dlat/2)**2 + cos(self.lat1) * cos(self.lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a)) 
        #r = 6371 # Radius of earth in kilometers. Use 3956 for miles
        return c * 3963.1676