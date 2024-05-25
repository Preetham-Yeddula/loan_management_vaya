from abc import ABC, abstractmethod

class IDataStore(ABC):
    @abstractmethod
    def add(self, key, value):
        pass

    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def update(self, key, new_value):
        pass