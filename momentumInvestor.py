import numpy as np
import math
import time
import random

class momentumInvestor:

    def __init__(self, id, money, confidence):
        self.investorId = id
        self.avaMoney = money
       
        self.buyOrders = np.array([('test company', 0)],
                      dtype=[('stock', 'U30'), ('quantity', 'i4')])
           # structured array to store outgoing orders, TRUE is buy FALSE is sell
        
        self.sellOrders = np.array([('test company', 0)],
                      dtype=[('stock', 'U30'), ('quantity', 'i4')])
        
        self.confidenceVal = confidence
        # a variable to influence the behavior of investors

        self.consecutiveIncrease = np.array([('test company', 0)],
                                   dtype= [('stock', 'U30'), ('increase', 'i4')])

        self.consecutiveDecrease = np.array([('test company', 0)],
                         dtype= [('stock', 'U30'), ('decrease', 'i4')])
        
        # counter variable to keeping track of decreases/increases
        self.counter = 0


    
    def buildPortfolio(self, stockData, company):
        """call to populate portfolio at
           the start of the simulation"""
        
        pass
        
    
    def determinePurchase(self, companyName, stockData):
       """reads in historical data from stock
          and apply strategy to decide purchases"""
       
       # track the consecutive increases/decreases in stock trends, resetting to zero if streak is broken

       if (self.consecutiveIncrease['increase'][self.consecutiveIncrease['stock'] == companyName] < (10 - self.confidenceVal) or
          self.consecutiveDecrease['decrease'][self.consecutiveIncrease['stock'] == companyName] < (10 - self.confidenceVal)):
           
        if stockData[-1] >= stockData[-2]:
            self.consecutiveIncrease['increase'][self.consecutiveIncrease['stock'] == companyName] += 1
            self.consecutiveDecrease['decrease'][self.consecutiveIncrease['stock'] == companyName] = 0

        else:
            self.consecutiveIncrease['increase'][self.consecutiveIncrease['stock'] == companyName] = 0
            self.consecutiveDecrease['decrease'][self.consecutiveIncrease['stock'] == companyName] += 1

       # after 10 consecutive increases (streak req decreased by confidence), 3 drops are tolerated, this is tracked by counter


         # checker for increases post initial streak
       if (self.consecutiveIncrease['increase'][self.consecutiveIncrease['stock'] == companyName] >= (10 - self.confidenceVal)):
          if stockData[-1] <= stockData[-2]:
             self.counter += 1
          else:
             self.consecutiveIncrease['increase'][self.consecutiveIncrease['stock'] == companyName] += 1
         
         # checker for decreases post initial streak
       elif self.consecutiveDecrease['decrease'][self.consecutiveIncrease['stock'] == companyName] >= (10 - self.confidenceVal):
           if stockData[-1] >= stockData[-2]:
             self.counter += 1
           else:
              self.consecutiveDecrease['decrease'][self.consecutiveIncrease['stock'] == companyName] += 1
         
         # clears tracking if 3 decrease/increase are observed
       if self.counter >= 3:
          self.counter = 0
          self.consecutiveDecrease['decrease'][self.consecutiveIncrease['stock'] == companyName] = 0
          self.consecutiveIncrease['increase'][self.consecutiveIncrease['stock'] == companyName] = 0

         # places orders if adequate increases/decreases are met
       if self.consecutiveIncrease['increase'][self.consecutiveIncrease['stock'] == companyName] >= (14 - self.confidenceVal):

            # TODO: Edit how much to sell or buy!
            # self.orders['quantity'][self.orders['stock'] == companyName] = self.confidenceVal
            # NEED TO CHECK IF THERE IS SUFFICIENT MONEY

          print(f'{companyName} at {stockData[-1]} purchased!')


       if self.consecutiveDecrease['decrease'][self.consecutiveIncrease['stock'] == companyName] >= (14 - self.confidenceVal):

          print(f'{companyName} at {stockData[-1]} sold!')

               
       return 