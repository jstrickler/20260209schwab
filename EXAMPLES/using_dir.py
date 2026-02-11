class Dog:
    def bark(self):
        print("woof! woof!")
    
    def wag(self):
        print("wag wag wag wag wag")

d = Dog()
print(f"{dir(d) = }\n")

colors = ["red", "purple", "black"]
attributes = [name for name in dir(colors) if not name.startswith('_')]
print(f"PUBLIC attributes: {attributes}\n")

x = 5
print(dir(x))

attr_name = "bark"
if hasattr(d, attr_name):
    m = getattr(d, attr_name)  # get the wag attribute of Dog instance d
    print(f"{type(m) = }")
    m()

setattr(Dog, 'growl', lambda self: print("grrrr"))
d.growl()

getattr(d, 'wag')()
d.wag()




