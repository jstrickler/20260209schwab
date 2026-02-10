from pprint import pprint

fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

f0 = []
for f in fruits:
    value = f.upper()
    f0.append(value)
print(f"{f0 = }\n")

#   [VALUE for VARIABLE in ITERABLE if CONDITION]
f1 = [f.upper() for f in fruits] # list comprehension
print(f"{f1 = }\n")

f2 = [f.upper() for f in fruits if f.startswith('p')]
print(f"{f2 = }\n")

f3 = [f for f in fruits if f.startswith('a')]
print(f"{f3 = }\n")

f4 = [f.upper() if f.startswith('p') else f.lower() for f in fruits]
print(f"{f4 = }\n")

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]
 
dob1 = [p[-1] for p in people]
print(f"{dob1 = }\n")

dob2 = [(p[1], p[-1]) for p in people]
print(f"{dob2 = }\n")

dob3 = [(p[1], p[-1]) for p in people if p[-1] < '1965']
print(f"{dob3 = }\n")

with open('DATA/breakfast.txt') as food_in:
    all_foods = food_in.read().splitlines()
print(f"{all_foods = }\n")

no_spam = [food for food in all_foods if food.lower() != 'spam']
unique_foods = set(no_spam)
sorted_unique = sorted(unique_foods, key=str.lower)
print(f"{sorted_unique = }\n")

fruit_list = [f.upper() for f in fruits]
print(f"{fruit_list = }\n")

fruit_gen = (f.upper() for f in fruits)
print(f"{fruit_gen = }")
for fruit in fruit_gen:
    print(fruit)

