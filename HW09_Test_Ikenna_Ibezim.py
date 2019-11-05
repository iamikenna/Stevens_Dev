"""
Author: Ibezim Ikenna
Test cases for User functions about date and time 
"""
import os, unittest
from HW09_Ikenna_Ibezim import Repository, Instructor, Student

class TestRepository(unittest.TestCase):
    """Test cases for all the functions"""
    def test_Student(self):
        """ testing the student function with the expected output in every case"""
        directory = "/Users/ikenna/Downloads/se810"
        expect = {"/Users/ikenna/Downloads/se810/test_student.txt":
                        {'cwid': 10103, 'name': "Baldwin, c", 'Dept': "SFEN", 'course': "SSW 567" }}
        # fa = Repository(directory)
        # self.assertEqual(fa._students['10103'].name, "Baldwin, C")
        # self.assertEqual(fa._students['10103'].major, "SFEN")
        # self.assertEqual(fa._students['10103'].completed_courses, [çourse1, ])
        
        # , expect)
        # expect = {"/Users/ikenna/Downloads/se810/test_student.txt":
        #         {'cwid': 10103, 'name': "Baldwin, c", 'Dept': "SFEN", 'course': "SSW 567" }}
        # self.assertEqual(fa._students, expect)
    
def main():
    """
    Test cases
    """  
    pass
 
if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
