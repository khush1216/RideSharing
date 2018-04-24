# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 13:16:47 2018

@author: singh
"""
import networkx as nx
from networkx import bipartite 

class MaxMatching:
    def getMergedRides(self,combinedRideWithDist):
        mergeableTripGraph= nx.Graph();
        mergeableTripGraph.add_weighted_edges_from(combinedRideWithDist)
        matching_dictionary = nx.max_weight_matching(mergeableTripGraph, maxcardinality=True)
        
        #print(matching_dictionary) 
        return matching_dictionary
    
    def getMergedRidesWithSavedDist(self,mergedRides,distSavedList):
        mergedRidesWithSavedDist = dict()
        
        for item in mergedRides:
            trip = str(item[0]) + "," + str(item[1])
            dist = distSavedList.get(trip)
            mergedRidesWithSavedDist[trip] = dist

        return mergedRidesWithSavedDist
    
    

#g = GraphMatching::Graph::WeightedGraph[
#  [1, 2, 10],
#  [1, 3, 11]
#]
#m = g.maximum_weighted_matching
#print(m.edges)
##=> [[3, 1]]
#print(m.weight(g))
##=> 11