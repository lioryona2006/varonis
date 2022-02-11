from dataclasses import dataclass
from Person import Person
from collections import UserList
class MagicList(UserList):
    def __init__(self, cls_type=None):
        self.data = []
        self._cls_type = cls_type

    def __setitem__(self, index, value):
        if index > len(self.data):
            raise IndexError()
        if index < len(self.data):
            self.data[index] = value
        if index == len(self.data):
            self.data.append(value)

    def __getitem__(self, index):
        if index > len(self.data):
            raise IndexError()
        if index < len(self.data):
            return self.data[index]
        if index == len(self.data):
            if self._cls_type:
                self.data.append(self._cls_type())
        return self.data[index]

