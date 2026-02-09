import json

with open('../DATA/presidents.json') as presidents_in:
    presidents_data = json.load(presidents_in)

for president in presidents_data:
    name = president['lastname'] + ', ' + president['firstname']
    party = president['party']
    print(f'{name:40s} {party}')
