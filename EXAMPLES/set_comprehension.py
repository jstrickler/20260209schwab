import re

FILE_PATH = "../DATA/alice.txt"

# NOTE: r'\W+' is a regular expression that splits on anything that isn't a letter, number, or underscore

with open(FILE_PATH) as mary_in:
    file_contents = mary_in.read()
    # new_set = {VALUE for VARIABLE in ITERABLE if CONDITION}
    s = {w.lower() for w in re.split(r'\W+', file_contents) if w} # Get unique words from file. Only one line is in memory at a time. Skip "empty" words.
print(s)
print()

fruits = ['pomegranate', 'cherry', 'apricot', 'Apple', 'Orange', 'orange',
'lemon', 'Kiwi', 'ORANGE', 'lime', 'Watermelon', 'guava', 'CHERRY',
'Papaya', 'FIG', 'pear', 'banana', 'Tamarind', 'Persimmon', 
'elderberry', 'peach', 'BLUEberry', 'lychee', 'GRAPE', 'date' ]

fruit_set = {f.lower() for f in fruits}
print(f"{fruit_set = }\n")
