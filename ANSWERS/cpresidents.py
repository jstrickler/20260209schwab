import csv

with open('../DATA/presidents.csv') as presidents_in:
    rdr = csv.reader(presidents_in)
    for row in rdr:
        print(f'{row[1]:25s} {row[2]:12s} {row[-1]}')
