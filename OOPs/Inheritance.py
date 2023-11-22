class Animal:
    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")


class Rabbit(Animal):
    def rabbit_run(self):
        print("Rabbit is Running")


class Fish(Animal):
    def fish(self):
        print("Fish is Swimming")


class Hawk(Animal):
    def fly(self):
        print("Hawk is flying")


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()


print(rabbit.alive)
fish.eat()
hawk.sleep()
rabbit.rabbit_run()
fish.fish()
hawk.fly()

