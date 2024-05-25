from .DataStoreInterface import IDataStore

class DictDataStore(IDataStore): # implementing DataStore Interface
    def __init__(self, data_dict):
        if(not isinstance(data_dict, dict)):
            self.data = {}
        self.data = data_dict

    def add(self, key, value):

        self.data[key] = value
        print(key)
        print(value)

    def get(self, key: str):
        print(key)
        print(self.data.get(key))
        return self.data.get(key)

    def update(self, key, new_value):
        if key in self.data:
            self.data[key] = new_value