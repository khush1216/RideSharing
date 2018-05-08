# RideSharing
An Algorithm for Ridesharing

1. The project can be run by running testdoc.py
This is run on the new-york data set for the month of January which contains about 97L records. The data needs to preprocessed according to what has been mentioned in the report and
arranged according to the columns mentioned in RideDetailsClass.py

2. Details about the files:

    a. RideDetailsClass - This contains methods that returns the location dictionary, fareAmount, passenger Count, drop time, offset (that would skip the records initially considered without having to read through them again) and the original distance for the ride
                          which will help calculate the final saved distance.
                          
    b. EuclideanDistClass - Calculates the euclidean distance obtained between the data returned from the Ride Details Class.
                            This returns a dictionary of Euclidean distance between sources and destinations, trips to be sent to the next pool,
                            trips whch need to be sent to the osrm server both sources and destinations and trips with passenger count = 3
                            which will be sent as individual trips.
                        
    c. DistSaved Class - This will return  a dictionary of the all combinations of rides which were sent to the osrm server and return the best 
                         possible combinations of all trips with the distance saved as the values and the combination of trip ids as the keys.
                         These will be used as weights for the MaxMatiching algorithm
                      
     d. MaxMatching Class - This will treat all the trips ids sent to it as nodes and the saved distance as weights and return a set of trips 
                            to be merged that would be a bst possible match.
                          
     e. CombineRides and CombineRidesWithMultithreading - Contain other methods for combining rides.
     
     f. DbConnection Class - Connects to the MySQL database and disconnects once the data is collected. 
     
 3. To run the code, the user will need to install OSRM on his machine (local installation is necessary as it will ensure faster processing of
    all records). The user will also need to store the Yellow taxi cab data into a MySQL database, filter out columns with passenger count > 3
    add Trip_ids and re-arrange the column data types according to the data type required - for example, STRING to TIMESTAMP/DATETIME,
    latitude, longitude geometry to DOUBLE, etc.
    
4. The user will need to download new-york-latest.osrm data file to run OSRM on the local machine. Once installed, this can be run using
    osrm-routed new-york-latest.osrm command on the command line.
