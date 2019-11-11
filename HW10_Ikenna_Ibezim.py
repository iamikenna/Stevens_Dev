"""
Author: Ibezim Ikenna
User functions about stevens student repository
"""
import os
from file_reader import file_reading_gen
from prettytable import PrettyTable
from collections import defaultdict

class Student:
    """Creating a class to define the functions of the students and store the details"""

    def __init__(self, cwid, name, dept):
        """Representing and storing the values in self"""

        self._cwid, self._name, self._dept = cwid, name, dept # declaring each details of the student
        self._courses = dict() #_courses[course]= grade
        
    def add_course(self, course, grade):
        """Storing the grade associated with a course for this student"""
        if (grade in ['A', 'A-', 'B+', 'B', 'B-', 'C+',  'C']):
            self._courses[course] = grade # so we created a function for getting the grade and course and adding it both into a dictonary for later use 


class Instructor:
    """Creating a class to define the functions of the Instructor and store the details"""

    def __init__(self, cwid, name, dept):
        """Representing and storing the values in self"""

        self._cwid, self._name, self._major = cwid, name, dept
        self._courses = defaultdict(int) #_courses[course]= no of student

    def get_student_no(self, course):
        """Function to create a default dictionary and save the courses and number of students taking each course"""

        self._courses[course] += 1 #adding the course and no of student to the default dictionary

class Major:
    """Creating a class to store and access the majors and courses taken by each student"""

    def __init__(self, dept, r_e, course):
        """Function to represent the dept, required courses and electives to be taken"""

        self.dept = dept
        self._electives = set()
        self._required = set()
        

class Repository:
    """Creating a class to define the functions of the students and store the details"""
    """
    Students
    instructor
    """


    def __init__(self,path, ptable=False):
        """Function to represent the parameters of the class student and instructor"""
        
        self._majors = dict() #storing the 
        self._students = dict() #students[cwid]=student()
        self._instructor = dict() #instruction[cwid]= instructions()

        self._get_majors(os.path.join(path, "majors.txt"))
        self._get_students(os.path.join(path, "students.txt"))
        self._get_instructor(os.path.join(path, "instructors.txt"))
        self._get_grades(os.path.join(path, "grades.txt"))
       
        if ptable: 
            self.major_prettytable()
            self.student_prettytable()
            self.instructor_prettytable()

    def _get_majors(self, path):
        """Getting the grades details from the file path"""
        try:
            for maj, r_e, course in file_reading_gen(path,3, sep='\t',header=True): # looping the major, required or elective and the dept
                # print(course)
                if maj not in self._majors.keys():
                    self._majors[maj] = Major(maj, r_e ,course)
                   
                if r_e == "R":
                    self._majors[maj]._required.add(course) # addding courses to the 
                elif r_e == "E":
                         self._majors[maj]._electives.add(course)
        except ValueError as ik:
            print(f"There was an error {ik} after attempting to get student details at {course}")
       
    def _get_students(self, path):
        """Getting the student details from the file path"""

        try:
            for cwid, name, dept in file_reading_gen(path, 3, sep=';', header=True):
                self._students[cwid] = Student(cwid, name, dept)
        except FileNotFoundError:
            print(f"Cant find any file ")
        except ValueError:
            print(f"Wrong value for student with {cwid}")

    def _get_instructor(self, path):
        """Getting the instructors details from the file path"""
        
        try:
            for cwid, name, dept in file_reading_gen(path, 3, sep='|', header=True):
                self._instructor[cwid] = Instructor(cwid, name, dept)
        except FileNotFoundError:
            print(f"Cant find files")
        except ValueError:
            print(f"cant find any other details related to {cwid}")

    def _get_grades(self, path):
        """Getting the grades details from the file path"""

        try:
            for cwid, course, grade, instructor_cwid in file_reading_gen(path,4, sep='|',header=True):
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

    def major_prettytable(self):
        pretty_table3 = PrettyTable(field_names=['Dept', 'Required', 'Electives'])
        for maj2 in self._majors.values():
            pretty_table3.add_row([maj2.dept, maj2._required, maj2._electives])

        print(pretty_table3)
    
    def student_prettytable(self):
        
        pretty_table = PrettyTable(field_names=['CWID', 'Name', 'Major', 'Completed Courses', 'Remaining Courses', 'Remaining Electives'])
        for student in self._students.values():            
            pretty_table.add_row([student._cwid, student._name, student._dept, sorted(student._courses.keys()), sorted(self._majors[student._dept]._required-student._courses.keys()), (self._majors[student._dept]._electives-student._courses.keys() if len(self._majors[student._dept]._electives-student._courses.keys())==3 else None)])

        print(pretty_table)
 
    def instructor_prettytable(self):
        pretty_table2 = PrettyTable(field_names=['CWID', 'Name', 'Dept', 'Course', 'Students'])
        for Instructor in self._instructor.values():
            for cour in Instructor._courses:
                pretty_table2.add_row([Instructor._cwid, Instructor._name, Instructor._major, cour, Instructor._courses[cour]])

        print(pretty_table2)
        

def main():
    """
    Test cases
    """  
    stevens = Repository("/Users/ikenna/Downloads/se810", ptable=True)
    print(stevens)                                                                                                                                                                                                                                                                                                                                                                                            
if __name__ == "__main__":
    main()
