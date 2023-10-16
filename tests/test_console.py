!/usr/bin/python3
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
    class_unfound = "** class doesn't exist **\n"

    def setUp(self):
        """Setup for Basic Tests"""
        self.cmd = HBNBCommand()
        self.file_path = "console.py"

    def testPycodestyleCoding(self):
        """Check for pycodestyle compliance"""
        style = pycodestyle.StyleGuide(quiet=False)
        p = style.check_files([self.file_path])
        self.assertEqual(p.total_errors, 0, 'Fix pycodestyle'

    def tearDown(self):
        """Cleaning Up testing"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def testQuit(self):
        """The wuit command """
        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("quit")
            self.assertEqual('', stdout.getvalue())

    def testEmptyLine(self):
        """Testing empty input"""
        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("\n")
            self.assertEqual('', stdout.getvalue())

    def testAll(self):
        """Test the all command """
        with patch('sys.stdout', new=StringIO()) as stdout:
            self.cmd.onecmd("all octopus")
            self.assertEqual(TestHBNBCommand.class_unfound,
                             stdout.getvalue())
        with patch('sys.stdout', new=String()) as stdout:
            self.cmd.onecmd("all State")
            self.assertEqual("[]\n", stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
