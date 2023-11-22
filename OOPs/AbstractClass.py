from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def go(self):
        print("You can drive the car")

    def stop(self):
        print("Fucking Car is stopped")


class Motorcycle(Vehicle):

    def stop(self):
        print("Fucking Motorcycle  is stopped")

    def go(self):
        print("You ride the Motorcycle")


# vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()
# vehicle.go()
car.go()
motorcycle.go()
car.stop()
motorcycle.stop()