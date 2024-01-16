import math
import time
import multiprocessing
import numpy as np

class market:

    def init(self):
        buyQueue = np.array([],
                      dtype=[('stock', 'U30'), ('quantity', 'uint32'), ('ID', 'i4')])

        sellQueue = np.array([],
                      dtype=[('stock', 'U30'), ('quantity', 'uint32'), ('ID', 'i4')])
        
        # keeps track of transfered money & stock in a time frame
        transferedMoney = 0
        transferedStock = 0

        stockPrice = 10


    def updateQueues(self, buyOrders, sellOrders):
        """Updates the list of all orders 
        from investors"""
    
        self.buyQueue = np.concatenate([self.buyQueue, buyOrders])
        self.sellQueue = np.concatenate([self.sellQueue, sellOrders])


    def sortQueues(self):
        """sorts the queues
           called after investors send in orders"""

        # buy queue is sorted to prioritize highest price first
        self.buyQueue.sort(order= "price")[::-1]

        # sell queue is sorted to prioritize lowest ask first
        self.sellQueue.sort(order= "price")


    def updateMarket(self, investorList, stockData):
        """matches and carry out ALL buy and sell orders"""

        for i in self.buyQueue:
            self.executeOrder(self.buyQueue[i], investorList, stockData)

    def updateMarketPrice(self):
        """calculates a market price to display
           clears transferedMoney/Stock when used"""
        
        self.stockPrice = round(self.transferedMoney / self.transferedStock, 2)
        self.transferedMoney = 0
        self.transferedStock = 0

    def executeOrder(self, highestOrder, investorList, stockData):
        """executes one buy order in the queue
            highestOrder is an data point in buyQueue
            NEVER CALL THIS, ITS ONLY FOR UPDATEMARKET"""

    
        highestOrder["quantity"] - self.sellQueue[0]["quantity"]
        
        # update & gives out the money to the buyers & sellers
        startSellQuantity = self.sellQueue[0]["quantity"]
        self.sellQueue[0]["quantity"] - highestOrder["quantity"]

        # take the difference between start and end quantity to get money & stock transfered
        investorList[self.sellQueue[0]['ID']].avaMoney += (startSellQuantity - self.sellQueue[0]["quantity"]) * stockData[-1]
        investorList[highestOrder['ID']].avaMoney -= (startSellQuantity - self.sellQueue[0]["quantity"]) * stockData[-1]

        # tracks the transfered items
        self.transferedMoney += (startSellQuantity - self.sellQueue[0]["quantity"]) * stockData[-1]
        self.transferedStock += (startSellQuantity - self.sellQueue[0]["quantity"])


        # deletes the buy order if it is emptied
        if self.buyQueue[0]["quantity"] == 0:
            self.buyQueue = np.delete(self.buyQueue, 0)

        # base case, ends recursion when buy order cleared
        if highestOrder["quantity"] == 0:

            return True;

        # alternative base case,  ends recursion if sell queue is empty
        elif self.sellQueue.size() == 0:

            return False;

        else:
            return self.executeOrder(highestOrder)


            
