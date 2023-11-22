class Car:
    color = None


class Motorcycle:
    color = None


def change_Color(vehicle, color):
    vehicle.color = color


car_1 = Car()
car_2 = Car()
bike_1 = Motorcycle()
car_3 = Car()
change_Color(car_1, "red")
change_Color(car_2, "white")
change_Color(car_3, "blue")
change_Color(bike_1,"Black")


print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)
