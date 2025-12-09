import curses
from domains import *
from guiInput import prompt

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


def guiOutput(stdscr, classroom, courses):
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
            return
