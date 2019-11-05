"""
Author: Ibezim Ikenna
User functions about stevens student repository
"""
import os
from HW08_Ikenna_Ibezim import file_reading_gen
from prettytable import PrettyTable
from collections import defaultdict

class Student:
    """Creating a class to define the functions of the students and store the details"""

    def __init__(self, cwid, name, dept):
        """Representing and storing the values in self"""
        self._cwid, self._name, self._dept = cwid, name, dept
        self._courses = dict() #_courses[course]= grade
        
    def add_course(self, course, grade):
        """Storing the grade associated with a course for this student"""
      
        self._courses[course] = grade

    
   
class Instructor:
    """Creating a class to define the functions of the Instructor and store the details"""
    
    def __init__(self, cwid, name, dept):
        """Representing and storing the values in self"""
        self._cwid, self._name, self._major = cwid, name, dept
        self._courses = defaultdict(int) #_courses[course]= no of student

    def get_student_no(self, course):
        """Function to create a default dictionary and save the courses and number of students taking each course"""
        self._courses[course] += 1
  

class Repository:
    """Creating a class to define the functions of the students and store the details"""
    """
    Students
    instructor
    """
    def __init__(self,path, ptable=False):
        """Function to represent the parameters of the class"""

        self._students = dict() #students[cwid]=student()
        self._instructor = dict() #instruction[cwid]= instructions()
        self._get_students(os.path.join(path, "students.txt"))
        self._get_instructor(os.path.join(path, "instructors.txt"))
        self._get_grades(os.path.join(path, "grades.txt"))

        if ptable:
            self.student_prettytable()
            self.instructor_prettytable()
       
    def _get_students(self, path):
        """Getting the student details from the file path"""
        try:
            for cwid, name, dept in file_reading_gen(path, 3, sep='\t', header=False):
                self._students[cwid] = Student(cwid, name, dept)
        except FileNotFoundError:
            print(f"Cant find files or any details for student with {cwid}")
        except ValueError:
            print(f"cant find any other details related to {cwid}")

    def _get_instructor(self, path):
        """Getting the instructors details from the file path"""
        try:
            for cwid, name, dept in file_reading_gen(path, 3, sep='\t', header=False):
                self._instructor[cwid] = Instructor(cwid, name, dept)
        except FileNotFoundError:
            print(f"Cant find files or any details for instructor with {cwid}")
        except ValueError:
            print(f"cant find any other details related to {cwid}")

    def _get_grades(self, path):
        """Getting the grades details from the file path"""
        try:
            for cwid, course, grade, instructor_cwid in file_reading_gen(path,4, sep='\t',header=False):
                if cwid in self._students.keys():
                    self._students[cwid].add_course(course, grade)
                else: 
                    print(f"dint find student with {cwid}")
           
                if instructor_cwid in self._instructor.keys():
                        self._instructor[instructor_cwid].get_student_no(course)
                else:
                    print(f"didnt find prof {instructor_cwid} whose course was mentioned")
        except ValueError:
            print("Not getting the details for the user")

    def student_prettytable(self):
        """ A function display out put  """
        
        pretty_table = PrettyTable(field_names=['CWID', 'Name', 'Dept', 'Courses'])
        for student in self._students.values():
            pretty_table.add_row([student._cwid, student._name, student._dept, sorted(student._courses.keys())])
        print(pretty_table)
        
    def instructor_prettytable(self):
        """ A function display out put"""
    
        pretty_table = PrettyTable(field_names=['CWID', 'Name', 'Dept', 'Courses','Students'])
        for Instructor in self._instructor.values():
            for i in Instructor._courses:
                pretty_table.add_row([Instructor._cwid, Instructor._name, Instructor._major, i, Instructor._courses[i]])
        print(pretty_table)

def main():
    """
    Test cases
    """  
    stevens = Repository("/Users/ikenna/Downloads/se810", ptable=True)
    print(stevens)                                                                                                                                                                                                                                                                                                                                                                                            
if __name__ == "__main__":
    main()

