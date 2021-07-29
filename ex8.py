""""You working in a shipment company. Your manager asked from you to design a program that allows them to enter items 
weight in order to be saverd in the shipment file. Your program should have a sentinel value, if the user finished adding
all the items, then he will enter the sentinel value to stop the program"""

#i will make it that it will create a dictionary of key items and values weight and that create a .txt 

import os

def create_dictionary():
    
    dic_of_items = {}
    entrada = ''
    while entrada != '0':
        entrada = input("input the name of the item: ")
        if entrada == '0':
            break
        else:
            try:
                dic_of_items[entrada] = float(input(f"enter the weight in kg of {entrada}: "))
                if dic_of_items[entrada] <= 0:
                    raise Exception
            except:
                print("input a valid weight")
    
    return dic_of_items

def create_a_txt(dic_of_items):

    dir_path = os.path.dirname(os.path.realpath(__file__))
    writetext = open(dir_path + '/' + "items.txt", "w")
    for key , value in dic_of_items.items():
            writetext.write(f"{key}̣  ____  {value} kg" + os.linesep)
    
    print(f"txt created")


if __name__ == '__main__':
    dic_of_items = create_dictionary()
    create_a_txt(dic_of_items)
