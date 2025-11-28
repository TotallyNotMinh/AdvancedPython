def initClass(numOfStudent):
    classList = [];
    print("-- Getting Students --")
    for i in range(0, numOfStudent):
        sName = input("Enter student name: ")
        sId = input("Enter student id: ")
        sDoB = input("Enter DoB: ")
        student = {"name": sName, "Id": sId, "DoB": sDoB}
        classList.append(student)
    return classList

def listStudent(classList):
    print("-- Student List --")
    for i in classList:
        print(f"Name: {i["name"]}, Id: {i["Id"]}, DoB: {i["DoB"]}.")

def initStudentMark():
    sName = input("Enter student name: ")
    sMark = input("Enter student mark: ")
    
    return {"name": sName, "mark": sMark}

def initCourseList(numOfCourse):
    courseList = [] 
    print("-- Getting Courses --")
    for i in range(0, numOfCourse):
        cName = input("Enter course name: ")
        cId = input("Enter course ID: ")
        numOfStudent = int(input("Enter number of student: "))
        mark = []

        for i in range(0, numOfStudent):
            mark.append(initStudentMark())

        courseList.append({"name": cName, "Id": cId, "mark": mark})
    return courseList

def getCourseMark(cName, courses):
    for course in courses:
        if course["name"] == cName:
            for mark in course["mark"]:
                print(f"Name: {mark["name"]}, Mark: {mark["mark"]}")


if __name__ == "__main__":
    myClass = initClass(5)
    listStudent(myClass)
    courses = initCourseList(3)
    getCourseMark("Calculus", courses)
