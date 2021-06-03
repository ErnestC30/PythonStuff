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
        self.small = small
        self.med = med
        self.large = large

    def addCar(self, type):
        if type == 1:
            if self.small > 0:
                self.small -= 1
                return True
            else:
                return False
        if type == 2:
            if self.med > 0:
                self.med -= 1
                return True
            else:
                return False
        if type == 3:
            if self.large > 0:
                self.large -= 1
                return True
            else:
                return False
        
ps = parkingSystem(2,1,0)
print(ps.addCar(1))
print(ps.addCar(1))
print(ps.addCar(1))
print(ps.addCar(2))
print(ps.addCar(3))
