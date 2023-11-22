from Car import car

car_1 = car("Chevy", "Corvette", 2021, "Blue")
car_2 = car("Ford", "Mustang", "2022", "Red")
'''print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)'''
car.wheels = 2325500
car_1.wheels = 2

'''car_1.stop()
car_2.drive()'''
print(car_1.wheels)
print(car_2.wheels)
print("Class Variable: ", car.wheels)
