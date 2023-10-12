#!/usr/bin/python3
"""
    This module defines unittests for models/base_model.py.
    """

import unittest
from datetime import datetime
from models import BaseModel
import models


class Test_BaseModel(unittest.TestCase):
    """
    This tests cases and attributes of BaseModel class.
    """

    def test_instances(self):
        """
        This test that the BaseModel instance has the expected attributes.
        """
        test_model = BaseModel()
        self.assertEqual(type(test_model.id), str)
        self.assertEqual(type(test_model.created_at), datetime)
        self.assertEqual(type(test_model.updated_at), datetime)

    def test_str_method(self):
        """
        This tests the __str__ method of the BaseModel instance.
        """
        t_model = BaseModel()
        output_str = "[BaseModel] ({}) {}".format(t_model.id, t_model.__dict__)
        self.assertEqual(str(t_model), output_str)

    def test_save_method(self):
        """
        This tests the save method of the BaseModel instance.
        """
        test_model = BaseModel()
        test_model.updated_at = datetime.fromtimestamp(0)

        test_model.save()

        self.assertNotEqual(test_model.updated_at, datetime.now())

    def test_dict_method(self):
        """
        This tests the to_dict method of the BaseModel instance.
        """
        mymodel = BaseModel()
        my_dict = mymodel.to_dict()
        self.assertEqual(type(my_dict), dict)
        self.assertEqual(my_dict["__class__"], "BaseModel")
        self.assertEqual(my_dict["id"], mymodel.id)
        self.assertEqual(my_dict["created_at"], mymodel.created_at.isoformat())
        self.assertEqual(my_dict["updated_at"], mymodel.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
