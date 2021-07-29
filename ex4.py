""""Your teacher asked from you to write a program that allows her to enter student 4 exam result and then the program
calculates the average and displays whether student passed the semester or no.in order to pass the semester, the average 
score must be 50 or more"""

def amount_of_results():
    while True:
        try:
            count = int(input("type the amount of result to calculate the average: "))
            if count <= 0:
                raise Exception
            return count
        except:
            print("input error, must be a number greater that 0 and a integer")

def result_input(count):
    result_list = []

    while True:
        try:
            note = int(input(f"type the {count}° note (o to 100): "))
            if 0<= note and note <= 100:
                result_list.append(note)
                count -= 1
                if count == 0:
                    break
            else:
                raise Exception
        except:
            print("invalid number, must go from 0 to 100")

    return result_list

def prom(result):
    sum = 0
    for notes in result:
        sum = sum + notes
    promedio = int(sum/(len(result)))
    print(f"the average of the results is: {promedio}")
    return promedio

def pass_failed(average):
    if average < 50:
        print("the student does not pass ")
    if average > 50:
        print("the student does pass")

if __name__ == '__main__':
    count = amount_of_results()
    result = result_input(count)
    average = prom(result)
    pass_failed(average)
