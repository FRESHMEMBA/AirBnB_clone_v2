#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""


import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    # def all(self, cls=None):
    #     """Returns the list of objects of one type of class"""

        # if cls is not None:
        #     return {key: value for key, value
        #         in FileStorage.__objects
        #         if cls in key
        #         }
        # return FileStorage.__objects
    def all(self, cls=None):
        """Returns the list of objects of one type of class"""
        new_dict = {}
        if cls is not None:
            for key, value in FileStorage.__objects.items():
                if cls in key:
                    new_dict[key] = value
            return new_dict
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Deletes an object from __objects if it's inside
        """
        if obj is not None:
            key = f"{type(obj).__name__}.{obj.id}"
            self.__objects.pop(key, None)
    # def delete(self, obj=None):
    #     """Deletes an object from __objects if it's inside"""
    #     if obj is not None:
    #         key = obj.__class__.__name__ + '.' + obj.id
    #         if key in self.__objects:
    #             del self.__objects[key]

    def close(self):
        """
        Call reload() method for deserializing the JSON file to objects
        """
        self.reload()