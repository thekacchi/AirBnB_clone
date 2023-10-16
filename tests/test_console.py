#!/usr/bin/python3
"""HBNBCommand Tests"""

import unittest
import console
import os
import sys
import pycodestyle
from unittest.mock import patch
from consile import HBNBCommand
import maths


class TestingHBNBCommand(unittest.TestCase):
    """Testing the console"""

    def setUp(self):
        """Setup for Basic Tests"""
        self.cmd = HBNBCommand()
        self.file_path = "console.py"

    def tearDown(self):
        """Cleaning Up testing"""
        try:
            os.remove("file.json")
        except Exception:
            pass

if __name__ == '__main__':
    unittest.main()
