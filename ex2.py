"""Design a program that allows your teacher to enter the result of three exam and it shows the average score"""

#modify to calculate any prom from 0 to 100 of amy amount of results

def amount_of_results():
    while True:
        try:
            count = int(input("type the amount of result to calculate the prom"))
            if count <= 0:
                raise Exception
            return count
        except:
            print("input error")

def result_input(count):
    result_list = []

    while True:
        try:
            note = int(input(f"type the {count} note (o to 100): "))
            if 0<= note and note <= 100:
                result_list.append(note)
                count -= 1
                if count == 0:
                    break
            else:
                print("must go 0 to 100")
        except:
            print("invalid number")

    return result_list

def prom(result):
    sum = 0
    for notes in result:
        sum = sum + notes
    promedio = int(sum/(len(result)))
    print(f"the prom of the results is: {promedio}")
    



if __name__ == '__main__':
    count = amount_of_results()
    result = result_input(count)
    prom(result)