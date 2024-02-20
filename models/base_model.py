#!/usr/bin/python3
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
        if len(kwargs):
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = value

    def __str__(self):
        return f"{[__class__.__name__]} {(self.id)} {self.__dict__}"

    def save(self):
        current_date = datetime.now()
        self.updated_at = current_date.strftime("%Y-%m-%dT%H:%M:%S.%f")

    def to_dict(self):
        dict_converter = self.__dict__.copy()
        dict_converter['created_at'] = self.created_at
        dict_converter['updated_at'] = self.updated_at
        dict_converter['__class__'] = self.__class__.__name__
        return dict_converter
