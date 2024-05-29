class Flaxem:

    day="Saturday"
    def move(self):
        print(f"{self.day} is moving")


obj=Flaxem()

obj.move()

class call:
    def __init__(sm,name,age):
        sm.name=name
        sm.age=age

    def agree(sm):
       print(f"{sm.name} is {sm.age} years old")


cm=call("Mutumba",24)
cm.agree()

print(cm.name)

class Dog:

    # Class Variable
    animal = 'dog'

    # The init method or constructor
    def __init__(self, breed, color):

        # Instance Variable
        self.breed = breed
        self.color = color


# Objects of Dog class
Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")

print('Rodger details:')
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)

print('\nBuzo details:')
print('Buzo is a', Buzo.animal)
print('Breed: ', Buzo.breed)
print('Color: ', Buzo.color)

# Class variables can be accessed using class
# name also
print("\nAccessing class variable using class name")
print(Dog.animal)  