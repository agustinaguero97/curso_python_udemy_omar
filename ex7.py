"""You are software developer. One of your clients is weather forecasting company. They asked from you to design a program
that allows them to enter the temperature for the whole week. After that the program will show the hottest day and coldest
day in that week"""

def temp_per_day(day):
    count = 1
    list_of_temp = []
    while (day+1) != count:
        try:
            temp = float(input(f"enter the temperature of the {count}° day: "))
            count += 1
            list_of_temp.append(temp)

        except:
            print("temp input invalid")

    return list_of_temp 

def day_input():
    while True:
        try:
            day = int(input("input amount of days "))
            if day <= 0:
                raise Exception
            return day
        except:
            print("day input invalid")

def hottest_coldest(list_of_temps):
    list_of_sorted_temps = sorted(list_of_temps)
    hottest = list_of_sorted_temps[(len(list_of_sorted_temps)-1)] #in a list of 3 elements the len will be 3 but the las element will be 2
    coldest = list_of_sorted_temps[0]
    return hottest,coldest



def wich_day_is_the_hottest_coldest(hottest,coldest,list_of_temps):
    for items in range(len(list_of_temps)):

        if hottest == list_of_temps[items]: #if are two days repeat the temp and are coldest/hottest, it will print it twice as the hottest/coldest
            print (f"the {items+1}° day is the hottest with {hottest}°C") 
        if coldest == list_of_temps[items]:
            print (f"the {items+1}° day is the coldest with {coldest}°C")



if __name__ == '__main__':
    day = day_input()
    list_of_temps = temp_per_day(day)
    hottest,coldest= hottest_coldest(list_of_temps)
    wich_day_is_the_hottest_coldest(hottest,coldest,list_of_temps)

    




