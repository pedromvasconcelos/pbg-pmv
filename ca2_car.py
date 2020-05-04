# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 20:33:58 2018

@author: 99993
"""
import pandas as pd

class Car(object):
    
    def __init__(self):
        self.__colour = ''
        self.__make = ''
        self.__model = ''
        self.__mileage = 0
        self.engineSize = ''

    def setColour(self, colour):
        self.__colour = colour

    def getColour(self):
        return self.__colour

    def setMake(self, make):
        self.__make = make

    def getMake(self):
        return self.__make

    def setModel(self, model):
        self.__model = model

    def getModel(self):
        return self.__model

    def setMileage(self, mileage):
        self.__mileage = mileage

    def getMileage(self):
        return self.__mileage

    def move(self, distance):
        print('Moved ' + str(distance) + 'kms')
        self.__mileage = self.__mileage + distance

    def paint(self, colour):
        print('Getting a paint job - new colour is: ' + colour)
        self.__colour = colour

class ElectricCar(Car):
    
    def __init__(self):
        Car.__init__(self)
        self.__numberFuelCells = 1
        
    def getNumberFuelCells(self):
        return self.__numberFuelCells
    
    def setNumberFuelCells(self, numberFuelCells):
        self.__numberFuelCells = numberFuelCells
        
class HybridCar(Car):
    
    def __init__(self):
        Car.__init__(self)
        self.__numberFuelCells = 1
        self.__engineSize = ''
        
    def getNumberFuelCells(self):
        return self.__numberFuelCells
    
    def setNumberFuelCells(self, numberFuelCells):
        self.__numberFuelCells = numberFuelCells        

    def getEngineSize(self):
        return self.__engineSize
    
    def setEngineSize(self, engineSize):
        self.__engineSize = engineSize
        
class PetrolCar(Car):
    
    def __init__(self):
        Car.__init__(self)
        self.__engineSize = ''
        
    def getEngineSize(self):
        return self.__engineSize
    
    def setEngineSize(self, engineSize):
        self.__engineSize = engineSize
        
class DieselCar(Car):
    
    def __init__(self):
        Car.__init__(self)
        self.__engineSize = ''
        
    def getEngineSize(self):
        return self.__engineSize
    
    def setEngineSize(self, engineSize):
        self.__engineSize = engineSize        

class CarFleet(object):
    
    def __init__(self):
        self.__petrol_cars = []
        self.__electric_cars = []
        self.__diesel_cars = []
        self.__hybrid_cars = []
        for i in range(1, 21):
            self.__petrol_cars.append(PetrolCar())
        for i in range(1, 7):
            self.__electric_cars.append(ElectricCar())
        for i in range(1, 11):
            self.__diesel_cars.append(DieselCar())
        for i in range(1, 5):
            self.__hybrid_cars.append(HybridCar())            

    def getPetrolCars(self):
        return self.__petrol_cars

    def getElectricCars(self):
        return self.__electric_cars
    
    def getHybridCars(self):
        return self.__hybrid_cars
    
    def getDieselCars(self):
        return self.__diesel_cars
    
    def checkCarsInStock(self):
        stock = pd.read_csv('car_stock.csv')

        print('Number of Petrol Cars : ', stock.at[0,'Current Stock'])
        print('Number of Diesel Cars : ', stock.at[1,'Current Stock'])
        print('Number of Hybrid Cars : ', stock.at[2,'Current Stock'])
        print('Number of Electric Cars : ', stock.at[3,'Current Stock'])
        
    def write_csv(self):
        df = pd.DataFrame({'Type of car':['Petrol', 'Diesel', 'Hybrid', 'Electric'],
                           'Initial Stock':[20,10,4,6],
                           'Current Stock': [str(len(self.getPetrolCars())),
                                              str(len(self.getDieselCars())),
                                              str(len(self.getHybridCars())),
                                              str(len(self.getElectricCars()))]})
        df.to_csv('car_stock.csv', index = False)
        
    def rent(self, type):
        if type == 'P':
            return self.__petrol_cars.pop()
        elif type == 'D':
            return self.__diesel_cars.pop()
        elif type == 'H':
            return self.__hybrid_cars.pop()        
        elif type == 'E':
            return self.__electric_cars.pop()

    def returnCar(self, type, car):
        if type == 'P':
            self.__petrol_cars.append(car)
        elif type == 'D':
            self.__diesel_cars.append(car)
        elif type == 'H':
            self.__hybrid_cars.append(car)
        elif type == 'E':
            self.__electric_cars.append(car)

    def mainMenu(self):
        print('Welcome to Europcar')
        rentedCar = None
        msg = 'Would you like to rent a car R, return a car U, any key to quit?'
        answer = input(msg)
        while answer == 'R' or answer == 'U':
            if answer == 'R':
                type = input('What car would you like to rent? -\nP for petrol;\nD for Diesel;\nH for Hybrid;\nE for electric\n please enter one of the above letters:  ')
                rentedCar = self.rent(type)
                self.write_csv()
            elif answer == 'U':
                type = input('What car would you like to return -\nP for petrol;\nD for Diesel;\nH for Hybrid;\nE for electric\n please enter one of the above letters:  ')
                self.returnCar(type, rentedCar)
                self.write_csv()
            self.checkCarsInStock()
            answer = input(msg)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
