"""Write a program that gives the percentage of student who passed in a class and the percentage of students who failed in a class"""

def students():
    while True:
        try:
            passed = int(input("enter the amount of students who pass: "))
            failed = int(input("enter the amount of students who fails: "))
            if passed < 0 or failed < 0:
                raise Exception
            return passed,failed
        except:
            print("input a  number above 0")

def percentage(students_P,students_F):
    all_students = students_F + students_P
    passed_percentage = (students_P * 100)/all_students
    print(f"the percentage of students who passed of {all_students} total is: {passed_percentage}%")
    print(f"the percentage of students who failed of {all_students} total is: {100-passed_percentage}%")


if __name__ == '__main__':
    students_P , students_F = students()
    percentage(students_P,students_F)
    
