from momentumInvestor import momentumInvestor
from reversionInvestor import reversionInvestor
import pandas as pd
import numpy as np


# FOLLOWING ARE TEST VARIABLES
L1 = list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


buyOrders = np.array([('Comp A', 2, 1), ('Comp B', 5, 1), ('Comp C', 2, 1)],
                      dtype=[('stock', 'U30'), ('quantity', 'i4'), ('ID', 'i4')])

        
sellOrders = np.array([('Comp B', 5, 1), ('Comp A', 5, 1), ('Comp C', 5, 1)],
                      dtype=[('stock', 'U30'), ('quantity', 'i4'), ('ID', 'i4')])


def startInvestorTests():

    reversionInvestorTest()
    

    return
    

def momentumInvestorTests():
    Investor = momentumInvestor(1, 2000, 5)

    historical_prices = list(range(0, 15))

    historical_prices.extend(list(range(15, 0, -1)))

    print (historical_prices)

    print('expected:')
    print("""
test company at 7 purchased!
test company at 8 purchased!
test company at 9 purchased!
test company at 10 purchased!
test company at 11 purchased!
test company at 12 purchased!
test company at 13 purchased!
test company at 14 purchased!
test company at 15 purchased!
test company at 8 sold!
test company at 7 sold!
test company at 6 sold!
test company at 5 sold!
test company at 4 sold!
test company at 3 sold!
test company at 2 sold!
          """)
    

    print("actual:")


    for i in range(0, len(historical_prices) - 2):

     Investor.determinePurchase('test company', historical_prices[0:i + 2])

     return

    

def reversionInvestorTest():
   
    historical_prices = list([100, 100 ,100, 115, 115, 130, 130, 130, 130, 130, 130, 130, 130])

    RevInvestor = reversionInvestor(1, 100, 5)

    for i in range(0,len(historical_prices) + 2):
       if i % 3 == 0:
          RevInvestor.getAverage(historical_prices[0:i + 2])
       RevInvestor.determinePurchase('test company', historical_prices[0:i + 2])
