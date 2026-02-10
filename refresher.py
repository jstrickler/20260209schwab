x = 5
y = x
print(x, y)
x = 10
print(x, y)

colors = ['pink', 'purple', 'green']
print(f"{colors[0] = }")
print(f"{colors[:2] = }")

c2 = colors
c2.append('blue')
print(f"{colors = }")
print(f"{c2 = }")
c3 = list(colors)
c4 = colors[::]
c2.append('black')
print(f"{colors = }")
print(f"{c2 = }")
print(f"{c3 = }")
print(f"{c4 = }")

value: int = 123
print(f"{value = }")
value = "abc"
print(f"{value = }")

def foo(a: int):
    print(a)

foo("abc")

x = 5
print(f"{dir(x) = }")
print(x.bit_length())
x = 23985720395820358
print(f"{x.bit_length() = }")

name = "Charles Schwab"
print(f"{name[0] = }")
print(f"{name[4:7] = }")

stuff = {'a': 5, 'm': 9, 'c': 10}
more_stuff = {'z': 8, 'r': 19}

stuff |= more_stuff
print(f"{stuff = }")
print('-' * 60)

target = 'x'
for color in colors:
    if color.startswith(target):
        print(color.upper())
        break
else:
    print("Not found")

b_colors = [color.upper() for color in colors if color.startswith(target)] or (print("NOT FOUND"), [])[1]
print(f"{b_colors = }")
