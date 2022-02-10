poly_data_different_val_types = [{'data': [{'key': 'key1', 'val': 'val1', 'valType': 'str'}]},
                                 {'data': [{'key': 'key1', 'val': 5, 'valType': 'int'}]}, {'data': [{'key': 'key1', 'val': 5.55, 'valType':'float'}]}]

poly_data_wrong_keys = [{'data1': [{'key': 'key1', 'val': 'val1', 'valType': 'str'}]},{'data': [{'key1': 'key1', 'val': 'val1', 'valType': 'str'}]},{'data': [{'key': 'key1', 'val1': 'val1', 'valType': 'str'}]},{'data': [{'key1': 'key1', 'val': 'val1', 'valType1': 'str'}]}]

poly_data_wrong_schema = [{'x':5,'data1': [{'key': 'key1', 'val': 'val1', 'valType': 'str'}]},{'data': {'key': 'key1', 'val': 'val1', 'valType': 'str'}},[{'data': {'key': 'key1', 'val': 'val1', 'valType': 'str'}}],{'data': [{'test':'test','key': 'key1', 'val': 'val1', 'valType': 'str'}]}]

poly_data_extra_keys = [{'data': [{'key': 'key1', 'val': 'Ly', 'valType': 'str','m':10}]},{'data': [{'Proc':5},{'key': 'key1', 'val': 'Ly', 'valType': 'str'}]}]