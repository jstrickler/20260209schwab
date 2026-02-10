colors = list()
colors.append('red')
colors.append('black')

states = []  #  states = list()
states.append('Utah')
states.append('Iowa')


value = 38.7    #  value = float(38.7)

class Animal:
    def move(self):
        print("moving...")

class Dog(Animal):
    def bark(self):
        print("woof! woof!")

d1 = Dog()
d2 = Dog()
d1.bark()
d2.bark()
d1.move()

