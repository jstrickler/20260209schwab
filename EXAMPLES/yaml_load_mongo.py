from pprint import pprint
import yaml

with open('../DATA/mongo.yaml') as mongo_in:
    mongo_data = yaml.load(mongo_in, Loader=yaml.Loader)

pprint(mongo_data)


