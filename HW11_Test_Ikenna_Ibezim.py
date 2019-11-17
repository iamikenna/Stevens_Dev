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
from HW11_Ikenna_Ibezim import Student, Instructor, Repository, Major

class RepositoryTest(unittest.TestCase):
    """ Class test for Repository """
    def test_major(self):
        """function to test the major tables""" 
        repository = Repository("/Users/ikenna/Downloads/se810/hw11 files")
        e_requirement,  e_electives = {'SFEN': {'SSW 810', 'SSW 540', 'SSW 555'}, 'CS': {'CS 570', 'CS 546'}}, {'SFEN': {'CS 546', 'CS 501'}, 'CS': {'SSW 810', 'SSW 565'}}
        o_required, o_electives  = {},  {}
        for dept in repository._majors:
            o_required[dept] = (repository._majors[dept]._required)
            o_electives[dept] = (repository._majors[dept]._electives) 
        self.assertEqual(e_requirement,o_required)
        self.assertEqual(e_electives,o_electives)

    def test_instructor_db(self):
        """function to test the instructor tables from the database in sqlite"""
        repository = Repository("/Users/ikenna/Downloads/se810/hw11 files")
        expected, output = [('98762', 'Hawking, S', 'CS', 'CS 501', 1), ('98762', 'Hawking, S', 'CS', 'CS 546', 1), ('98762', 'Hawking, S', 'CS', 'CS 570', 1), ('98763', 'Rowland, J', 'SFEN', 'SSW 555', 1), ('98763', 'Rowland, J', 'SFEN', 'SSW 810', 4), ('98764', 'Cohen, R', 'SFEN', 'CS 546', 1)],[] #Storing the expected and the result
        for dept in repository._second.keys():
            output.append(dept)
        self.assertEqual(expected, output) #comparing the expected values with the data from the database

    
class StudentTest(unittest.TestCase):
    """Testing class for student data"""  
    def test_student(self):
        """ Test Student summary table """
        student = Student("10103", "Jobs, S", "SFEN" )
        major = Major("SFEN","mem","kje")
        self.assertEqual(student._cwid, "10103")
        self.assertEqual(student._name, "Jobs, S") 
        self.assertEqual(student._dept, "SFEN") 
        self.assertEqual(major._electives, set())
        self.assertEqual(major._required, set())
        self.assertEqual(student._courses, {})

class InstructorTest(unittest.TestCase):
    """Test class for instructor data"""
    def test_instructor(self): 
        """Test Instructor summary table"""
        instructor = Instructor("98762",  "Hawking, S",  "CS")
        self.assertEqual(instructor._cwid, "98762")
        self.assertEqual(instructor._name, "Hawking, S")
        self.assertEqual(instructor._major, "CS") 
        self.assertEqual(instructor._courses, {}) #testing for the courses and number of students taking it 
        
            
if __name__ == "__main__":
    unittest.main(exit = False, verbosity = 2)  