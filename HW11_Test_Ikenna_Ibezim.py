"""
Author: Ibezim Ikenna
User functions to test the Repository sytem
"""
import os
import sqlite3
from file_reader import file_reading_gen
from prettytable import PrettyTable
from collections import defaultdict
import unittest
from HW11_Ikenna_Ibezim import Student, Instructor, Repository


class RepositoryTest(unittest.TestCase):
    """ Class test for Repository """
    def test_repository(self):
        stevens = Repository("/Users/ikenna/Downloads/se810/hw11 files", ptable=True)
        
        expected = {'SFEN': {'R': ['SSW 555', 'SSW 810', 'SSW 540', 'SSW 567'], 'E': ['CS 546', 'CS 501']}, 'CS': {'R': ['CS 546', 'CS 570'], 'E': ['SSW 810', 'SSW 565']}}
        output = stevens.major_prettytable
        self.assertEqual(expected, output)




if __name__ == "__main__":
    unittest.main(exit = False, verbosity = 2)  