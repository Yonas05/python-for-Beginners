class Duck:
    def walk(self):
        print("The Duck is Walking")

    def talk(self):
        print("The duck is quacking")


class Chicken:
    def walk(self):
        print("The Chicken is walking")

    def talk(self):
        print("The chicken is clucking")


class Person():
    print("The Person is Idiot")

    def walk(self):
        print("Fuck walking")

    def talk(self):
        print("fuck talking")

    def catch(self, fuck):
        fuck.talk()
        fuck.walk()


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(person)
