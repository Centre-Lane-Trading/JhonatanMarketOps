from endpoint_helper import *


class feature_class:
    def __init__(self) -> None:

        # Start date for the range of dates the user wants data for
        self.id = ''
        self.db_name = ''
        self.units = ''
        self.display_name = ''
    
    def read_data(self, id_input, db_name_input, display_name_input, units_input):
        self.id = id_input
        self.db_name = db_name_input
        self.units = units_input
        self.display_name = display_name_input


data = simple_request_entities('feature', 20000)


display_name_features: list[feature_class] = []
db_name_features: list[feature_class] = []
for entry in data:
    feature = feature_class()
    feature.read_data(entry['id'], entry['name'], entry['display_name'], entry['unit'])
    if feature.display_name is not None:
        display_name_features.append(feature)
    else:
        db_name_features.append(feature)
print('display names')
for features in display_name_features:
    print(f'ID: {features.id}, Name: {features.db_name}, Display Name: {features.display_name}, Units: {features.units}')
# print('no display names')
# for features in db_name_features:
#     print(f'ID: {features.id}, Name: {features.db_name}, Display Name: {features.display_name}, Units: {features.units}')
    
    