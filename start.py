import Test
import stockSimulator
    
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
        stockSimulator.startSim()

    else:
        print ("invalid selection")
    
    


