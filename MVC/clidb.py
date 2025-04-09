# This should contain the view and controller from Courses

from courses import *

def createCourse():
    number=input("Please enter the new number for the course: ")
    return Course(None,number)

def doDelete():
    id=input("Please enter the id to delete: ")
    return Course(id,None)

def doUpdate():
    id=input("Please enter the id to update: ")
    number=input("Please enter the new course number: ")
    return Course(id,number)

def main():
    choice=""
    cs=Courses()
    while choice.upper()!="Q":
        print(cs.retrieve())
        print("1) Retrieve current courses")
        print("2) Add new course")
        print("3) Update a course")
        print("4) Delete a course")
        print("Q) Quit")
        choice=input("Enter your choice: ")
        if choice=="1":
            print(cs.retrieve())
        elif choice=="2":
            c=createCourse()
            cs.create(c)
        elif choice=="3":
            c=doUpdate()
            cs.update(c)
        elif choice=="4":
            c=doDelete()
            cs.delete(c)

if __name__ == "__main__":
	main()

'''
MVC: Model-View-Controller
# Model defines data structure (updates view)
# View defines display (UI) (sends input from user to controller)
# Controller contains control logic (sometimes directly updates view and manipulates model)
'''