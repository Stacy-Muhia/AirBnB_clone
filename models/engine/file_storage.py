#!/usr/bin/python3
"""
    This module defines the class FileStorage.
"""
import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes_dict = {
        "Amenity": Amenity,
        "BaseModel": BaseModel,
        "City": City,
        "Place": Place,
        "Review": Review,
        "State": State,
        "User": User
        }


class FileStorage:
    """
    Class FileStorage will be the storage for various objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns __objects dictionary."""
        return self.__objects

    def new(self, obj):
        """Takes the args and adds it to the __objects dict in
            the format "<class_name>.<object_id>
        Args:
            obj: objects"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + str(obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """Serializes objects in __objects then saves JSON in __file_path.
        """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json_objects = {}
            for key, value in FileStorage.__objects.items():
                json_objects[key] = value.to_dict()
            j = json.dumps(json_objects)
            file.write(j)

    def reload(self):
        """Deserializes and reloads from ojects from JSON file back
        to __objects dict.
        Raises:
            FileNotFound Error: if file is not found"""
        try:
            with open(FileStorage.__file_path, "r") as file:
                data = json.load(file)
                for value in data.values():
                    myclass = value["__class__"]
                    myclass = eval(myclass)
                    obj = myclass(**value)
                    self.new(obj)
        except FileNotFoundError:
            pass
