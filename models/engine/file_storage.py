#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.place import Place
from models.amenity import Amenity


'''File Storage Module'''


class FileStorage():
    """
    a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances
    """
    # privare class attributes
    __file_path = 'file.json'
    __objects = {}

    # public instance methods
    def all(self, cls=None):
        '''returns the dictionary __objects'''
        if cls:
            oneclassObjects = {}
            for key, value in FileStorage.__objects.items():
                valueClass = value.__class__
                if cls == valueClass:
                    oneclassObjects[key] = value

            return oneclassObjects
        return self.__objects

    def new(self, obj):
        '''
        creates the keys that will be stored in __objects
        as class_name.id
        # BaseModel.12323 = {object}
        '''
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        '''
        serializes a dict to a json file:
        in this case, __objects to the file.json

        steps:
        1. open file
        2. serialise dict
        3. write to file
        4. close file
        '''
        # this wont work as we cant serialise objects,
        # as __objects we have objects
        # we need to convert the objs to dicts
        '''
        with open(FileStorage.__file_path, 'w') as f:
            for obj in FileStorage.__objects:
                json.dump(obj, f)
        '''

        # convert objs to dict, to do this we can to_dict which
        # returns the dict representation of an obj.
        dic = {}
        for key, value in self.__objects.items():
            d = value.to_dict()
            dic[key] = d

        # now we dump into json file
        with open(self.__file_path, 'w') as f:
            json.dump(dic, f, indent=4)

    def reload(self):
        '''
        deserializes a json file to a dict:
        in this case, file.json to __objects

        only if the file exists, otherwise, do nothing
        1. open file
        2. deserialise dict
        4. close file
        '''

        try:
            # this not complete, as after loading the file we
            # need to parse it properly
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for key, v in data.items():
                    self.__objects[key] = eval(v['__class__'])(**v)

        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        deletes obj from __objects if it is inside
        if obj is equal to None, the method should not do anything
        """
        if obj is not None:
            for k, v in self.__objects.items():
                if v is obj:
                    break
            self.__objects.pop(k)
