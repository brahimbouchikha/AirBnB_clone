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
        self.assertEqual(type(FileStorage), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)
