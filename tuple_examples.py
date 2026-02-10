extra_person = ('Bill', 'Allen', 'BillCo', '1972-02-13')
extra_person = 'Bill', 'Allen', 'BillCo', '1972-02-13'
thing = 45,  # single value tuple
other_thing = ()   # empty tuple

def ham():
    return 5, 10   # NOT return [5, 10]

ham_info = ham()
print(ham_info[0], ham_info[1])  # , ham_info[2])

value1, value2 = ham()  # iterable unpacking
print(value1, value2)

first_name, last_name, product, dob = extra_person
print(last_name, dob)

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXT', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', 'Meta', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'git', '1969-12-28'),
]
print(f"{people[0] = }")
print(f"{people[0][0] = }")
print(f"{people[0][0][0] = }")

print(f"{len(people) = }")
print(f"{len(people[0]) = }")

# t1, t2, t3, ..., t13 = people
first_name, last_name, *product, dob = people[0]
print(f"{first_name = }")
print(f"{last_name = }")
print()

for person in people:
    first_name, last_name, *product, dob = person
    print(last_name)
print('-' * 60)

for first_name, last_name, *product, dob in people:
    print(last_name)

people.append(extra_person)

for first_name, last_name, *product, dob in people:
    print(first_name, last_name, product, dob)
print('-' * 60)

for first_name, last_name, *_ in people:
    print(first_name, last_name)

def draw_line(ch, size):
    print(ch * size)

draw_line('-', 50)
draw_line('*', 20)

data = '+', 75
draw_line(data[0], data[1])
draw_line(*data)  # draw_line('+', 75) 

from datetime import date
info = 2025, 9, 27
d = date(*info)
print(f"{d = }")

#  eggs(**some_dictionary)


