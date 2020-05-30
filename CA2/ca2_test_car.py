import unittest

from ca2_car import Car, CarFleet

dealership = CarFleet()

#test the car functionality
class TestCar(unittest.TestCase):

    def setUp(self):
        self.car = Car()

    def test_car_mileage(self):
        self.assertEqual(0, self.car.getMileage())
        self.car.move(15)
        self.assertEqual(15, self.car.getMileage())

    def test_car_make(self):
        self.assertEqual('', self.car.getMake())
        self.car.setMake('Ferrari')
        self.assertEqual('Ferrari', self.car.getMake())

    def test_car_colour(self):
        self.assertEqual('', self.car.getColour())
        self.car.paint('red')
        self.assertEqual('red', self.car.getColour())

if __name__ == '__main__':
    unittest.main()

class TestCarApp(unittest.TestCase):
    
    def setUp(self):
        self.dealership = CarFleet()
        
    #Testing Rental Process
    def testRentProcessed(self):
        self.assertTrue(self.dealership.rent('P'))#Testing Rent of car for P type, petrol
        
    #Testing Number of Initial Petrol Car Stock
    def testInitialPetrolCarsinStock(self):
        InitialPetrol = dealership.readInitialPetrolStock()
        self.assertEqual(InitialPetrol, 20)
        
    #Testing Number of Initial Hybrid Car Stock    
    def testInitialHybridCarsinStock(self):
        Initial = dealership.readInitialHybridStock()
        self.assertEqual(Initial, 4)
    
    #Test Current Stock function for Diesel and Electric Cars
    def testCurrentDieselStock(self):  
        self.assertEqual(dealership.DieselCarStock(), 10)
    
    def testCurrentElectricStock(self):  
        self.assertEqual(dealership.ElectricCarStock(), 6)        
                
    #Teste write CSV method and number of rows (with headers)
    def testRowNumersinCSV(self):
        self.dealership.write_csv()
        expected = 5
        file = open('car_stock.csv')
        result = len(file.readlines())
        self.assertEqual(expected, result)  
        file.close()
    
    #Test to check availability to Rent and Return
    def testAvailabilitytoRent(self):
        self.assertEqual(dealership.checkAvailableStockforRent('H'),4)
        self.assertEqual(dealership.checkAvailableStockforRent('D'),10)
        
    def testAvailabilitytoReturn(self):
        self.assertEqual(dealership.checkAvailableStockforReturn('H'),0)    
    
if __name__ == "__main__":
    unittest.main()      
    
