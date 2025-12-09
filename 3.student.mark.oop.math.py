import numpy as np
import curses

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



def prompt(stdscr, msg):
    stdscr.clear()
    stdscr.addstr(0, 0, msg)
    stdscr.addstr(2, 0, "> ")
    curses.echo()
    value = stdscr.getstr(2, 2).decode()
    curses.noecho()
    return value


def menu(stdscr, title, options):
    idx = 0
    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, title)
        stdscr.addstr(1, 0, "-" * len(title))

        for i, option in enumerate(options):
            if i == idx:
                stdscr.addstr(3 + i, 0, f"> {option}")
            else:
                stdscr.addstr(3 + i, 2, option)

        key = stdscr.getch()

        if key == curses.KEY_UP:
            idx = idx - 1
        elif key == curses.KEY_DOWN:
            idx = idx + 1
        elif key in (curses.KEY_ENTER, 10, 13):
            return idx



def main(stdscr):
    curses.curs_set(0)
    classroom = Class()
    courses = CourseList()

    sCount = int(prompt(stdscr, "Number of students: "))
    for i in range(sCount):
        name = prompt(stdscr, "Student name: ")
        Id = prompt(stdscr, "Student ID: ")
        dob = prompt(stdscr, "Student DoB: ")
        classroom.addStudent(name, Id, dob)

    cCount = int(prompt(stdscr, "Number of courses: "))
    for i in range(cCount):
        name = prompt(stdscr, "Course name: ")
        Id = prompt(stdscr, "Course ID: ")
        credit = int(prompt(stdscr, "Course credit: "))
        studentList = classroom.getStudents()
        course = Course(name, Id, credit, studentList)
        courses.addCourse(course)

        for student in classroom.getStudents():
            mark = float(prompt(stdscr, f"Enter mark for student name {student.getName()}, ID {student.getId()}"))
            course.setMark(student, mark)
        

    choices = [
        "View marks for a course",
        "View GPA ranking",
        "Exit"
    ]

    while True:
        choice = menu(stdscr, "Main Menu", choices)

        # View course marks
        if choice == 0:
            cName = prompt(stdscr, "Enter course name:")
            marks = courses.getMarks(cName)
            stdscr.clear()
            row = 2
            if marks is None:
                stdscr.addstr(0, 0, f"Course not found for {marks}!")
            else:
                stdscr.addstr(0, 0, f"Marks for {cName}")
                for sid, mark in marks.items():
                    stdscr.addstr(row, 0, f"{sid}: {mark}")
                    row += 1
            stdscr.addstr(row + 1, 0, "Press any key...")
            stdscr.getch()

        # GPA ranking
        elif choice == 1:
            ranking = sortGPA(classroom, courses.getCourses())
            stdscr.clear()
            stdscr.addstr(0, 0, "GPA Ranking")
            row = 2
            for sid, gpa in ranking.items():
                stdscr.addstr(row, 0, f"{sid}: GPA {gpa:.2f}")
                row += 1
            stdscr.addstr(row + 1, 0, "Press any key...")
            stdscr.getch()

        else:
            break


curses.wrapper(main)

