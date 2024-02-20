#!/usr/bin/python3
""" Storage class definition """

import json
from ..base_model import BaseModel

class FileStorage():
    ''' Modules to help in saving, serialization of instances
    to a JSON file and deserializes JSON file to instances'''

    __file_path = {}
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        obj = BaseModel()
        self.__objects = obj.id

    def save(self):
        dup_obj = FileStorage.__objects
        obj_dict = {obj: dup_obj[obj].to_dict() for obj in dup_obj.keys()}

        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as f:
                return json.load(f)
        except Exception as s:
            pass
