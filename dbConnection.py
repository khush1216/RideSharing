# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 14:48:29 2018

@author: Khushbu
"""

import mysql.connector

class DB_Connect:
    def dbConnection(self):
    
        cnx = mysql.connector.connect(user = 'root',password='password123!',host='localhost',database='ridesharing');
        #cursor = cnx.cursor();
        return cnx;

    def closeConnection(self,connectionObj):
        connectionObj.close();
    