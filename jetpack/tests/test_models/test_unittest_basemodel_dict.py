#!/usr/bin/python3
"""Unittest for basemodel class
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModelDict(unittest.TestCase):
    def test_recreation_from_dict(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()

# Recreating instance fromt eh dict representatikn
        my_new_model = BaseModel(**my_model.to_dict())
        my_new_model_name = "My First Model"

# Check if recreated instance matches original
        self.assertEqual(my_model.id, my_new_model.id)
        self.assertEqual(my_model.name, my_new_model_name)
        self.assertEqual(my_model.my_number, my_new_model.my_number)
        self.assertEqual(my_model.created_at, my_new_model.created_at)
        self.assertEqual(my_model.updated_at, my_new_model.updated_at)
        self.assertEqual(type(my_new_model.created_at), datetime)
        self.assertEqual(type(my_new_model.updated_at), datetime)        
