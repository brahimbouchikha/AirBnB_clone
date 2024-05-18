#!/usr/bin/python3
"""
base_model_test Module
"""


import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_init(self):
        obj1 = BaseModel()
        obj2 = BaseModel()

        self.assertNotEqual(obj1.id, obj2.id)
        self.assertIsNotNone(obj1.id)
        self.assertIsNotNone(obj1.created_at)
        self.assertIsNotNone(obj1.updated_at)

    def test_save(self):
        obj1 = BaseModel()

        initial_upd_at = obj1.updated_at
        current_upd_at = obj1.save()
        self.assertNotEqual(initial_upd_at, current_upd_at)

    def test_to_dict(self):
        obj1 = BaseModel()

        my_obj_dic = obj1.to_dict()
        self.assertIsInstance(my_obj_dic, dict)
        self.assertEqual(my_obj_dic["__class__"], "BaseModel")
        self.assertEqual(my_obj_dic["id"], obj1.id)
        self.assertEqual(my_obj_dic["created_at"], obj1.created_at.isoformat())

    def test_str(self):
        obj1 = BaseModel()
        self.assertTrue(str(obj1).startswith('[BaseModel]'))
        self.assertIn(obj1.id, str(obj1))
if __name__=="__main__":
     unittest.main()