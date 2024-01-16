from market import market
from momentumInvestor import momentumInvestor
from reversionInvestor import reversionInvestor
import numpy as np 
import concurrent.futures
import random as rd
from decimal import Decimal, getcontext

# set the environment for two digit decimal points
ctx = getcontext()
ctx.prec = 2

STARTING_MONEY = Decimal(10000.00)

# create list of investors

investorList = list()
companyOne = list([131, 138, 135, 135, 128, 129, 131, 130, 124, 126, 124, 123, 124, 118, 
                       121, 116, 116, 121, 123, 118, 113, 110, 115, 119, 116])


# creating the moment investors
for ID in range(0, 3):
    investorList.append(momentumInvestor(ID, 10000, rd.randint(1, 10)))
    
# creating the reversion investors
for ID in range(0, 3):
    investorList.append(reversionInvestor(ID, 10000, rd.randint(1,10)))


def startSim():
   with concurrent.futures.ProcessPoolExecutor() as executor:
       
       # every investor needs to determine purchase
       # FINISH THIS, INCLUDING HOW TO ACTUALLY RETURN STUFF IDK ETC
       results = [executor.submit(investorList[ID].determinePurchase("Company One", companyOne), 1) for ID in range(0, len(investorList))]


   






