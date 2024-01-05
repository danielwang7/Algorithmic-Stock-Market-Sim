import numpy as np
import math
import time
import random

class momentumInvestor:

    def __init__(self, id, money):
        self.id = id
        self.avaMoney = float(money)
        self.outgoingOrder = {
           'D' : 0,
           'I' : 0
             } # dictionary of outgoing order
        self.evaluationPeriod = 5
        self.evaluationRigor = 5
    
    def buildPortfolio(self, stockData, company):
        """call to populate portfolio at
           the start of the simulation"""
        
         # the evaluation period changes the timeframe reference to determine if a stock should be brought
        if self.money >= stockData[-1]:
           
           if ((stockData[-1] - stockData[-self.evaluationPeriod]) / (self.evaluationPeriod) > self.evaluationRigor):
              if random.random() < 0.5:
                 if company == 'GI':
                    self.outgoingOrder['I'] += 1

                 if company == 'GD':
                    self.outgoingOrder['D'] += 1

                    #TODO: THIS HAS TO BE FIXED
    

    def determinePurchase(self, stockData):
       """reads in historical data from stock
          and apply strategy to decide purchases"""
       
       for stock in self.stockCompany:
           if stock == 1:
               if self.stockPurPrice[stock.index()] < stockData [-1]:

                    #TODO: IMPLEMENT
            
                   self.money -= stockData[-1]
                   print(f"Buyer {self.id} bought at {stockData[-1]}, Money left: {self.money}")
            
               else:
                   print(f"Buyer {self.id} can't afford to buy at {stockData[-1]}, Money left: {self.money}")

    def determineSell(self):
        pass
    

                
 

    