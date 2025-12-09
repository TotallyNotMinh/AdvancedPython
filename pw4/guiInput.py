import curses
from domains import *

def prompt(stdscr, msg):
    stdscr.clear()
    stdscr.addstr(0, 0, msg)
    stdscr.addstr(2, 0, "> ")
    curses.echo()
    value = stdscr.getstr(2, 2).decode()
    curses.noecho()
    return value


def guiInput(stdscr, classroom, courses):
    curses.curs_set(0)

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
        




