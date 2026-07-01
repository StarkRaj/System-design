from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def printVehicle(self):
        pass

class TwoWheeler(Vehicle):
    def printVehicle(self):
        print("This is a Two Wheeler")

class FourWheeler(Vehicle):
    def printVehicle(self):
        print("This is a Four Wheeler")



class VehicleFactory:
    @abstractmethod
    def createVehicle(self):
        pass

class TwoWheelerFactory(VehicleFactory):
    def createVehicle(self):
        return TwoWheeler()

class FourWheelerFactory(VehicleFactory):
    def createVehicle(self):
        return FourWheeler()

class Client:
    def __init__(self,vehicleFactory):
        self.vehicleFactory = vehicleFactory
    def getVehicle(self):
        return self.vehicleFactory.createVehicle()

if __name__ == "__main__":
    two_wheeler_factory = TwoWheelerFactory()
    two_wheeler = two_wheeler_factory.createVehicle()
    two_wheeler.printVehicle()
    
    four_wheeler_factory = FourWheelerFactory()
    four_wheeler = four_wheeler_factory.createVehicle()
    four_wheeler.printVehicle()

    