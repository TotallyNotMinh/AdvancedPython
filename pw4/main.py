from guiInput import *
from guiOutput import *
import domains
import curses


def main(stdscr):
    classroom = Class()
    courses = CourseList()

    guiInput(stdscr, classroom, courses)
    guiOutput(stdscr, classroom, courses)

curses.wrapper(main)


