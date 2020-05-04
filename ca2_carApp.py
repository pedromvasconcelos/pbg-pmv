from ca2_car import Car, ElectricCar, PetrolCar, CarFleet, HybridCar, DieselCar

# myCar = Car()
# print(myCar)
     
# myCar.setColour('Red')
# print(myCar.getColour())

# myCar.setMake('Ferrari')
# print(myCar.getMake())

# myCar.setModel('Testarossa')
# print(myCar.getModel())

# myCar.setMileage(54)
# print(myCar.getMileage())

# yellowTaxi = Car()
# yellowTaxi.setMake('Toyota')
# yellowTaxi.setModel('Avensis')
# yellowTaxi.setMileage(120004)

# yellowTaxi.paint('Bright Yellow')
# yellowTaxi.move(5)

# print(yellowTaxi.getColour())
# print(yellowTaxi.getMileage())

# electric = ElectricCar()
# electric.setMake('Nissan')
# electric.setModel('Leaf')
# print(electric.getNumberFuelCells())
# print(electric.getMake())
# print(electric.getModel())
    
# petrol = PetrolCar()
# petrol.setMake('Ford')
# petrol.setModel('Focus')
# petrol.setEngineSize('1.6')
# print(myCar.engineSize)
# myCar.engineSize = '3.5'
# print(myCar.engineSize)

europcar = CarFleet()
# europcar.checkCarsInStock()
# petrol = europcar.rent('P')
# europcar.checkCarsInStock()
# electric = europcar.rent('E')
# europcar.checkCarsInStock()
# europcar.returnCar('P', petrol)
# europcar.checkCarsInStock()
# anotherElectric = europcar.rent('E')
# europcar.checkCarsInStock()
# europcar.returnCar('E', anotherElectric)
europcar.checkCarsInStock()

europcar.write_csv()


europcar.mainMenu()

    
