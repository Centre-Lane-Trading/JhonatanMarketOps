from backend.endpoint_helper import *


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


feature_json = simple_request_entities('feature', 20000)
feature_list: list[feature_class] = []
for entry in feature_json:
    feature = feature_class()
    feature.read_data(entry['id'], entry['name'], entry['display_name'], entry['unit'])
    feature_list.append(feature)

feature_dict = {
    obj.display_name if obj.display_name is not None else obj.db_name: obj
    for obj in feature_list
}

display_names_list = []
for feature in feature_dict.values():
    if feature.display_name:
        display_names_list.append(feature.display_name)

print(display_names_list)