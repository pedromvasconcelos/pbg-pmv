
from ca2_car import CarFleet


dealership = CarFleet()
dealership.write_csv() #initialize

def mainMenu():
    print('Welcome to DBS Rental Service')
    print('\n********\nThis is our current stock:')
    dealership.checkCarsInStock()
    Car = None
    msg = 'Would you like to rent a car or return a car?\n********\nPress:\nR - Rent\nU - Retur\nS - Check current cars in stockn\nany other key to quit'
    answer = input(msg)
    while answer == 'R' or answer == 'U' or answer =='S':
        if answer == 'R':
            type = input('What car would you like to rent? -\nP for petrol;\nD for Diesel;\nH for Hybrid;\nE for electric\n please enter one of the above letters:  ')
            amount = int(input('Please enter the amount of cars to Rent:  '))
            total = 0
            if dealership.checkAvailableStockforRent(type) < amount:
                print('Not enough cars available')
                break
            else:
                while total < amount:
                    dealership.rent(type)
                    total = total + 1
                dealership.write_csv()
        elif answer == 'U':
            type = input('What car would you like to return -\nP for petrol;\nD for Diesel;\nH for Hybrid;\nE for electric\n please enter one of the above letters:  ')
            amount = int(input('Please enter the amount of cars to Return:  '))
            total = 0
            if dealership.checkAvailableStockforReturn(type) < amount:
                print('The amounts to return is higher than initial stock available')
                break
                while total < amount:
                    dealership.returnCar(type, Car)
                    total = total + 1
                dealership.write_csv()
        elif answer == 'S':
            dealership.checkCarsInStock()            
        answer = input(msg)




mainMenu()

