import math
import numpy as np

class Student:
    def __init__(self, name, Id, dob):
        self.__name = name
        self.__Id = Id
        self.__dob = dob

    def getName(self):
        return self.__name

    def getId(self):
        return self.__Id

    def getDob(self):
        return self.__dob


class Class:
    def __init__(self):
        self.__studentList = []

    def addStudent(self, count):
        for i in range(count):
            name = input("Enter student name: ")
            Id = input("Enter student Id: ")
            dob = input("Enter student DoB: ")
            self.__studentList.append(Student(name, Id, dob))

    def getStudents(self):
        return self.__studentList


class StudentMark:
    def __init__(self, student, mark):
        self.__student = student      
        self.__mark = mark

    def __str__(self):
        return f"Name: {self.__student.getName()}, Mark: {self.__mark}"

    def getStudent(self):
        return self.__student

    def getMark(self):
        return self.__mark


class Course:
    def __init__(self, name, Id, credit, studentList):
        self.__name = name
        self.__Id = Id
        self.__credit = credit
        self.__marks = []
        self.__students = studentList   

    def setMarks(self):
        print(f"-- Inputting marks for course: {self.__name} --")
        for student in self.__students:
            mark = math.floor(float(input(f"Enter mark for student {student.getName()}: ")))
            self.__marks.append(StudentMark(student, mark))

    def getName(self):
        return self.__name

    def getMarks(self):
        return self.__marks


class CourseList:
    def __init__(self):
        self.__cList = []

    def addCourses(self, count, studentList):
        for i in range(count):
            name = input("Enter course name: ")
            Id = input("Enter course Id: ")
            credit = int(input("Enter course credit: "))

            course = Course(name, Id, credit, studentList)
            course.setMarks()

            self.__cList.append(course)

    def getMarks(self, cName):
        for course in self.__cList:
            if cName == course.getName():
                return course.getMarks()
        return None

def main():
    print("-- Initializing class --")
    myClass = Class()

    sCount = int(input("Enter number of students in class: "))
    myClass.addStudent(sCount)

    print("-- Initializing courses --")
    courses = CourseList()

    n = int(input("Enter number of courses: "))
    courses.addCourses(n, myClass.getStudents())

    checkCourse = input("Enter course name to get marks: ")
    marks = courses.getMarks(checkCourse)

    if marks is None:
        print("Course not found!")
    else:
        print(f"-- Marks for {checkCourse} --")
        for m in marks:
            print(m)

main()

