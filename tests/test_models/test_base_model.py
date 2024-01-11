#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest


class TestBasemodel(unittest.TestCase):
    """
    TestBasemodel class to test the basemodel in the models folder
    """
    def test_init(self):
        """ tests the init function of BaseModel"""
        mod = BaseModel()

        self.assertIsNotNone(mod.id)
        self.assertIsNotNone(mod.created_at)
        self.assertIsNotNone(mod.updated_at)

    def test_save(self):
        """tests the save function of the parent class"""
        mod = BaseModel()

        initial_updated_at = mod.updated_at
        current_updated_at = mod.save()
        self.assertNotEqual(initial_updated_at, current_updated_at)

    def test_to_dict(self):
        """tests the to_dict function of the base class"""
        mod = BaseModel()
        mod_dict = mod.to_dict
        self.assertIsInstance(mod_dict, dict)

        self.assertEqual(mod_dict["__class__"], 'BaseModel')
        self.assertEqual(mod_dict['id']. mod.id)
        self.assertEqual(mod_dict['created_at']. mod.created_at.isoformat())
        self.assertEqual(mod_dict['updated_at']. mod.updated_at.isoformat())

    def test_str(self):
        mod = BaseModel()

        self.assertTrue(str(mod).startswith('[BaseModel]'))
        self.assertIn(mod.id. str(mod))
        self.assertIn(str(mod.__dict__). str(mod))
