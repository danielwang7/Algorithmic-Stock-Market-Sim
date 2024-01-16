import numpy as np
import math
import time
import random

class reversionInvestor:

    def __init__(self, id, money, confidence):
        self.investorId = id
        self.avaMoney = money
       
       # structured array to store outgoing orders, TRUE is buy FALSE is sell
        self.buyOrders = np.array([('test company', 0)],
                      dtype=[('stock', 'U30'), ('quantity', 'i4')])
           
        
        self.sellOrders = np.array([('test company', 0)],
                      dtype=[('stock', 'U30'), ('quantity', 'i4')])
        
        # a variable to influence the behavior of investors
        self.confidenceVal = confidence

        
        # counter variable to keeping track of decreases/increases
        self.counter = 0

        self.averagePrice = 0 

        # determines the period used to observe the average
        self.averagePeriod = 4

        # determines the percent that must be exceeded for purchase/sell
        self.averageThreshhold = 0.05


    def buildPortfolio(self):
        pass
    
    def getAverage(self, stockData):
        """updates the internal stored
           average pricc"""
        
        if len(stockData) <= self.averagePeriod:
            self.averagePrice = sum(stockData) / len(stockData)
        else:
            self.averagePrice = sum(stockData[-4:]) / self.averagePeriod


    def determinePurchase(self, companyName, stockData):

        # THERE IS DEVISION BY ZERO BUG HERE HELP
        excess = stockData[-1] / self.averagePrice - 1

        if excess > self.averageThreshhold:
            self.buyOrders['quantity'][self.buyOrders['stock'] == companyName] += int((excess * 100 * self.confidenceVal))
            print(f"{int(excess * 100 * self.confidenceVal)} units of {companyName} purchased at {stockData[-1]}")

            self.getAverage(stockData)
        

    def determineSell(self, stockData):
        pass
