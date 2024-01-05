import Test
import market
    
if __name__ == "__main__":
    print ("-------------------------------")
    print ("Finance Project Menu Options")
    print ("-------------------------------")
    print ("1) Execute testing functions in test.py")
    print ("2) openMarket")
    
    choice = int(input())

    if choice == 1:
        Test.startInvestorTests()
    
    elif choice == 2:
        market.openMarket()

    else:
        print ("invalid selection")
    
    


