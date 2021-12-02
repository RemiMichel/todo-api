from abc import ABC, abstractmethod


class Dao(ABC):

    @abstractmethod
    def get(self, id):
        pass

    @abstractmethod
    def create(self, label):
        pass

    @abstractmethod
    def update(self, id, label, status):
        pass

    @abstractmethod
    def list(self):
        pass
