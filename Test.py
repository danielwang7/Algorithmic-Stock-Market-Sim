from momentumInvestor import momentumInvestor
import pandas as pd
import numpy as np



def startInvestorTests():

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
    
    

