#!/usr/bin/python3
"""Unittest for basemodel class
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """setup my first model
        """
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89

     def test_instance_creation(self):
         """test the creation of the instance
         """
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)


    def test_str_representation(self):
        """test the string representation
        """
        expected_str = "[BaseModel] ({}) {}".format(self.my_model.id,
                                                    self.my_model.__dict__)
        self.assertEqual(str(self.my_model), expected_str)

    def test_save_method(self):
        """test the save method
        """
        initial_updated_at = self.my_model.updated_at
        self.my_model.save()
        new_updated_at = self.my_model.updated_at
        self.assertNotEqual(initial_updated_at, new_updated_at)

    def test_to_dict_method(self):
        """ test the to_dict method
        """
        model_dict = self.my_model.to_dict()
        self.assertTrue('__class__' in model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertTrue('created_at' in model_dict)
        self.assertTrue('updated_at' in model_dict)
        self.assertTrue('id' in model_dict)
        self.assertTrue('name' in model_dict)
        self.assertTrue('my_number' in model_dict)
