import numpy as np

class Student:
    def __init__(self, name, Id, dob):
        self.__name = name
        self.__Id = Id
        self.__dob = dob
        self.__marks = {}

    def getName(self):
        return self.__name

    def getId(self):
        return self.__Id

    def getDob(self):
        return self.__dob

    def addMark(self, cName, mark):
        self.__marks[cName] = mark

    def getMarks(self):
        return self.__marks


class Class:
    def __init__(self):
        self.__studentList = []

    def addStudent(self, name, Id, dob):
        self.__studentList.append(Student(name, Id, dob))

    def getStudents(self):
        return self.__studentList


class Course:
    def __init__(self, name, Id, credit, studentList):
        self.__name = name
        self.__Id = Id
        self.__credit = credit
        self.__students = studentList #Student objects
        self.__marks = {}

    def setMark(self, student, mark):
        mark = round(mark, 1)
        student.addMark(self.__name, mark)
        self.__marks[student.getId()] = mark


    def getName(self):
        return self.__name

    def getMarks(self):
        return self.__marks

    def getCredit(self):
        return self.__credit

    def getStudentMark(self, sId):
        return self.__marks[sId]
    
class CourseList:
    def __init__(self):
        self.__cList = []

    def addCourse(self, course):
        self.__cList.append(course)

    def getMarks(self, cName):
        for course in self.__cList:
            if cName == course.getName():
                return course.getMarks()
        return None

    def getTotalCredit(self):
        creditSum = 0
        for course in self.__cList:
            creditSum += course.getCredit()
        return creditSum

    def getCourses(self):
        return self.__cList


def calGPA(sId, courseList):
    marks = [] 
    cCredits = []
    for course in courseList:
        marks.append(course.getStudentMark(sId))
        cCredits.append(course.getCredit())
    
    marks = np.array(marks)
    cCredits = np.array(cCredits)

    gpa = np.sum((marks * cCredits)) / np.sum(cCredits)

    return gpa


def sortGPA(classroom, courseList):
    gpaList = []

    for student in classroom.getStudents():
        sGPA = calGPA(student.getId(), courseList)
        gpaList.append((student.getId(), sGPA))

    gpaList.sort(key=lambda x: x[1], reverse=True)

    return dict(gpaList)


