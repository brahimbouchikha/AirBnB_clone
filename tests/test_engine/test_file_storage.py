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

if __name__ == "__main__":
	unittest.main()
