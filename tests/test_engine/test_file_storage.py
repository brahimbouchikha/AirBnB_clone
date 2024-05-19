#!/usr/bin/python3
"""
test_file_storage Module
"""

import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorageInstantiation(unittest.TestCase):
    """
        Testing instantiation of file storage.
        """

    def test_FileStorage_instantiation_no_args(self):
        storage = FileStorage()
        self.assertEqual(type(storage), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)
    def test_FileStorage_file_path_is_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

if __name__ == "__main__":
    unittest.main()
