class Validator():
    def __init__(self, object_id, data):
        self.object_id = object_id
        self.data = data

    def validate_types(self):
        if type(self.object_id) is not int:
            return False
        for data_item in self.data:
            if type(data_item['val']) is int and not data_item['valType'] =='int':
                    return False
            elif type(data_item['val']) is float and not  data_item['valType'] == 'float':
                    return False
            elif type(data_item['val']) is str and not data_item['valType'] == 'str':
                    return False
        return True
    def validate_missing_data(self):
        if not self.object_id:
            return False
        for data_item in self.data:
            if not data_item['val'] or not data_item[
                'valType']  or  not data_item['key'] :
                return False
        return True
#{'data': [{'key': 'key1', 'val': 'val1', 'valType': 'str'}]}
# j={'object_id': 13,'data': [{'key': 'key1', 'val': 'val1', 'valType': 'str'}]}
# j = {'object_id': 13, 'data': [{'key': 'key1', 'val': 1, 'valType': 'int'}]}
# v = Validator(**j)
# print(v.validate_types())
# data_type = getattr(__builtins__,'str')
# print(data_type)
