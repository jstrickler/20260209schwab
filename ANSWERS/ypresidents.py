import yaml

with open('../DATA/presidents.yaml') as presidents_in:
    presidents_data = yaml.load(presidents_in, Loader=yaml.BaseLoader)

for president in presidents_data:
    name = president['lastname'] + ', ' + president['firstname']
    party = president['party']
    print(f'{name:35s} {party}')
