#Multi Level Inheritance
class Animal:
    def speak(self):
        print("Animal Speaking")

class Dog(Animal):
    def bark(self):
        print("Vau vau vau vau ")

class ChildDog(Dog):
    def eat(self):
        print("Sab khanxa ")

class ChildChildDog(ChildDog):
    def sleep(self):
        print("Sleeping")
d=ChildDog()
d.speak()
d.bark()
d.eat()

chd=ChildChildDog()
chd.speak()
chd.eat()
chd.bark()
chd.sleep()