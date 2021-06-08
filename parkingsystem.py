"""
Design a parking system for a parking lot. The parking lot has three kinds of parking spaces: big, medium, and small, with a fixed number of slots for each size.

Implement the ParkingSystem class:
ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem class. 
The number of slots for each parking space are given as part of the constructor.
bool addCar(int carType) Checks whether there is a parking space of carType for the car that wants to get into the parking lot. 
carType can be of three kinds: big, medium, or small, which are represented by 1, 2, and 3 respectively. 
A car can only park in a parking space of its carType. 
If there is no space available, return false, else park the car in that size space and return true.
"""

class parkingSystem(object):
    def __init__(self, small, med, large):
        self.parkSys = [small, med, large]      #Store as list, since we know carType is either 1, 2 or 3. Faster than checking if statements
    
    def addCar(self, carType):
        self.parkSys[carType - 1] -= 1
        return self.parkSys[carType - 1] >= 0



ps = parkingSystem(2,1,0)
print(ps.addCar(1))
print(ps.addCar(1))
print(ps.addCar(1))
print(ps.addCar(2))
print(ps.addCar(3))
