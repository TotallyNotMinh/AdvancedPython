class Student:
    def __init__(self, name, Id, dob):
        self.__name = name
        self.__Id = Id
        self.__dob = dob

class Class:
    def __init__(self):
        self.__studentList = []

    def addStudent(self, count):
        for i in range(0, count):
            name = input("Enter student name: ")
            Id = input("Enter student Id: ")
            dob = input("Enter student DoB: ")
            self.__studentList.append(Student(name, Id, dob))

class StudentMark:
    def __init__(self, name, mark):
        self.__name = name
        self.__mark = mark
    
    def __str__(self):
        return f"Name: {self.__name}, mark: {self.__mark}" 

    def getName(self):
        return self.__name

    def getMark(self):
        return self.__mark

class Course:
    def __init__(self, name, Id, sCount):
        self.__name = name
        self.__Id = Id
        self.__sCount = sCount
        self.__marks = []

    def setMarks(self):
        for i in range(0, self.__sCount):
            name = input("Enter student name: ")
            mark = input("Enter student mark: ")
            self.__marks.append(StudentMark(name, mark))

    def getName(self):
        return self.__name

    def getMarks(self):
        for mark in self.__marks:
            return mark


class CourseList:
    def __init__(self):
        self.__cList = []

    def addCourses(self, count):
        for i in range(0, count):
            name = input("Enter course name: ")
            Id = input("Enter course Id: ")
            sCount = int(input("Enter student count: "))
            course = Course(name, Id, sCount)
            course.setMarks()
            self.__cList.append(course)
            

    def getMarks(self, cName):
        for course in self.__cList:
            if (cName == course.getName()):
                return course.getMarks()


if __name__ == "__main__":
    print("-- Initializing class --")
    myClass = Class()

    sCount = int(input("Enter number of student of class: "))
    print(f"-- Adding {sCount} students to class --")
    myClass.addStudent(sCount)

    print("-- Initializing courses")
    courses = CourseList()

    n = int(input("Enter number of courses: "))
    print(f"-- Adding {n} courses")
    courses.addCourses(n)

    checkCourse = input("Enter course name to get marks: ")
    print(courses.getMarks(checkCourse))


    
