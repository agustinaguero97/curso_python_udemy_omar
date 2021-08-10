"""Your teacher asked to write a program that allows her to save students name and their scores in a file, and also to read 
students name and socres that stored in that file. The program after the end of each procedure will ask the teacher
whether he wants to do another procedure. You decided to use dictionary for this program and then serialize it into a file"""


import os


def input_student():
    while True:
        try:
            student = str(input('enter the name of the student: '))
            return student
        except:
            print("input a valid name")

def input_score():
    while True:
        try:
            score = int(input(f'enter the score(1-100) of the student {student} :'))
            if score < 1 or score > 100:
                raise ValueError
            return score
        except:
            print('invalid score, must go from 1 to 100')

def another_input():
    while True:
        try:
            answer = str(input('what to add another student? (y/n):'))
            if answer != 'y' and answer != 'n':
                raise Exception
            else:
                if answer == 'y':
                    return True
                if answer == 'n':
                    return False
        except:
            print('invalid input')

def dic_of_students(student,score,dic_stu):
    
    dic_stu[student] = score
    return dic_stu

def create_a_txt(dic_stu):

    dir_path = os.path.dirname(os.path.realpath(__file__))
    writetext = open(dir_path + '/' + "student_score.txt", "w")

    for key , value in dic_stu.items():
            writetext.write(f"student: {key}̣  ____  score: {value} " + os.linesep)
    
    os.close
    
    print(f"txt created")





if __name__ == '__main__':
    dic_stu = {}
    respuesta = True
    while respuesta == True:
        student= input_student()
        score = input_score()
        dic_stu = dic_of_students(student,score,dic_stu)
        respuesta = another_input()
    create_a_txt(dic_stu)


    