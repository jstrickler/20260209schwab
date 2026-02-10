import sys
animal = "wombat" # global
x = 100

if x:
    y = 10
print(f"{y = }")



def ham():
    x = 5  # local
#    global m  # DO NOT DO THIS!!!
    m = 99
    print(x)
    print(animal)

ham()

# print(f"{m = }")


print(f"{x = }")

def print(*args):
    arg_list = [str(arg).upper() for arg in args]
    __builtins__.print(*arg_list)

x = "piano"
print('abc', x)
print()
