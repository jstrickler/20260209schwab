def eggs(stuff):
    return "spam"

r = eggs(22)
print(f"{r = }")

eggs(48)

#  wombat(1, 2, 'abc')
#  wombat(name="Derek", animal="Penguin")
#  wombat(1, 2, animal="wombat")

def grep1(search_term, file_path):
    found_lines = []
    with open(file_path) as file_in:
        for raw_line in file_in:
            if search_term in raw_line:
                found_lines.append(raw_line.rstrip('\n\r'))
    return found_lines

results = grep1('guy', 'DATA/parrot.txt')
for line in results:
    print(line)
print('-' * 60)

def grep2(search_term, *file_paths):
    found_lines = []
    for file_path in file_paths:
        with open(file_path) as file_in:
            for raw_line in file_in:
                if search_term in raw_line:
                    found_lines.append(raw_line.rstrip('\n\r'))
    return found_lines

results = grep2('lizard', 'DATA/parrot.txt', 'DATA/words.txt', 'DATA/alice.txt')
for line in results:
    print(line)
print('-' * 60)

#         req pos      opt pos      req named w/default
def grep3(search_term, *file_paths, ignore_case=False):
    found_lines = []
    if ignore_case:
        search_term = search_term.lower()
    for file_path in file_paths:
        with open(file_path) as file_in:
            for raw_line in file_in:
                if ignore_case:
                    search_line = raw_line.lower()
                else:
                    search_line = raw_line
                if search_term in search_line:
                    found_lines.append(raw_line.rstrip('\n\r'))
    return found_lines

results = grep3('lizard', 'DATA/parrot.txt', 'DATA/words.txt', 'DATA/alice.txt', ignore_case=True)
for line in results:
    print(line)
print('-' * 60)

def config(**config_values):
    for key, value in config_values.items():
        print(key, value)

config(folder="DATA", filename="alice.txt", animal="wombat")


def eggs(foo, bar):
    print(foo, bar)

eggs(10, 20)
eggs(foo=10, bar=20)
eggs(bar=20, foo=10)

def ham(*args, **kwargs):
    print(f"{args = }")
    print(f"{kwargs = }")
    print()

ham()
ham(1)
ham(1,2)
ham(color="blue")
ham(1, color="blue")
ham(1, 2, 3, color="blue", animal="naked mole rat")

