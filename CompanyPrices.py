import time
import math

class generalDonuts:
    
     def __init__(self):
        self.currentPrice = 0.0
        self.historyPrices = []

     def updateCurrentDonutPrice(self, currentWeek):
    
        basePrice = 100.0 * (3.0 * math.sin(currentWeek) + (currentWeek / 20.0) + 3.0) #equation for base price
        finalPrice = basePrice / 100.0 

        self.historyPrices.append(finalPrice)

        return finalPrice
     
class generalIcecream:
    
     def __init__(self):
        self.currentPrice = 0.0
        self.historyPrices = []

     def updateCurrentIcePrice(self, currentWeek):
    
        basePrice = 100.0 * (1.8 * math.sin((2.0 / 9.0) * currentWeek) + (currentWeek / 15) + 1.5) #equation for base price
        finalPrice = basePrice / 100.0

        self.historyPrices.append(finalPrice)

        return finalPrice

def priceCounter():
           
   bigDonut = generalDonuts()
   bigIce = generalIcecream()
   currentWeek = 0


   for seconds in range(300):
     
     donutPrice = bigDonut.updateCurrentDonutPrice(currentWeek)
     icePrice = bigIce.updateCurrentIcePrice(currentWeek)
     print(f'{donutPrice:.2}')
     print(f'{icePrice:.2}')

     currentWeek = currentWeek + 1
   
     time.sleep(2)
      

