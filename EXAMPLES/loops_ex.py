colors = ['red', 'green', 'blue', 'purple', 'pink', 'yellow', 'black']  # create a list

for color in colors:  # loop over list
    print(color)
print()

with open('../DATA/mary.txt') as mary_in:  # open text file for reading
    for line in mary_in:  # loop over lines in file
        print(line, end='')  # print line with extra newline
print()

while True:  # loop "forever"
    name = input("What is your name? ")  # read input from keyboard
    if name.lower() == 'q':
        break  # exit loop
    print("Welcome,", name)
