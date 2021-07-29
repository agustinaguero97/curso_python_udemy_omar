"""Design a program that converts student score into grades(a,b,c,d, and failed)"""



def score_input():
    while True:
        try:
            score = int(input("type your score to conver to grades: "))
            if score <= 0 and score < 100:
                raise Exception
            return score

        except:
            print("score input error")

def your_grade(puntaje,grades_value):
    for key in grades_value:
        for value in grades_value[key]:
            if puntaje == value:
                print(f"your grade is {key}")
            if puntaje < 60:
                 print("your grade is F")
                 break



if __name__ == '__main__':


    grades_value= {'A+': [100,99,98,97],
                'A' : [96,95,94,93],
                'A-': [92,91,90],
                'B+': [89,88,87],
                'B' : [86,85,84,83],
                'B-': [82,81,80],
                'C+': [79,78,77],
                'C' : [76,75,74,73],
                'C-': [72,71,70],
                'D+': [69,68,67],
                'D' : [66,65,64,63],
                'D-': [62,61,60],
                }

    puntaje = score_input()
    your_grade(puntaje,grades_value)




    
