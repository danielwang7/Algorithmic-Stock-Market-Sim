import math
import time
import multiprocessing
import numpy as np


buyQueue = np.array([],
                      dtype=[('stock', 'U30'), ('quantity', 'i4'), ('ID', 'i4')])

sellQueue = np.array([],
                      dtype=[('stock', 'U30'), ('quantity', 'i4'), ('ID', 'i4')])

buyOrders = np.array([('Comp A', 2, 1), ('Comp B', 5, 1), ('Comp C', 2, 1)],
                      dtype=[('stock', 'U30'), ('quantity', 'i4'), ('ID', 'i4')])

        
sellOrders = np.array([('Comp B', 5, 1), ('Comp A', 5, 1), ('Comp C', 5, 1)],
                      dtype=[('stock', 'U30'), ('quantity', 'i4'), ('ID', 'i4')])
                      


def updateQueue(buyOrders, sellOrders):
    """Updates the list of all orders 
       from all investors, sorted by price"""
    
    #buyQueue + buyOrders
    #sellQueue + sellOrders

    # NEED A WAY TO APPEND STRUCTURED ARRAYS
    # NEED  A WAY TO SORT BY PRICE


    return

    
    
    


def executeTransactions():
    pass


def main():
    
    updateQueue(buyOrders, sellOrders)
