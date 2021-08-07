"""write a code for guessing game. In which the computer will guess a number and asks from the player to find the guess.
The player given 7 chances to find that number. Hint will given to the player when his guess is higher or lower than computer
guess. At the end of each game ask from the user whether he wants to play again. Every time the user guess is correct he
will get a point, otherwise computer will get point"""

import random

def create_a_number(min,max):
    return random.randint(min,max)

def player_guess(min,max):
    while True:
        try:
            guess = int(input(f"guess my number that goes {min} to {max}: "))
            if guess < 1 or guess > 100:
                raise Exception
            return guess
        except:
            print("invalid guess, try again")

def evaluation(guess,random_number,intentos,min,max):
    if random_number == guess:
        print("You did it!")
        return 0,0
    if random_number < guess:
        print(f"my number is lower that {guess}: ")
        max = guess
        return min,max

    if random_number > guess:
        print(f"my number is greater that {guess}: ")
        min = guess
        return min,max

def interface():
    print("Chose the game mode\n you guest the number (1)\n the machine guest the number (2)\n")
    while True:
        try:
            respuesta = int(input('chose your option'))
            if respuesta == 1:
                adivina()
                break
            if respuesta == 2:
                adivinador()
                break
            else:
                raise Exception
        except:
            print('invalid input')


def adivina():
    intentos = 7
    min = 1
    max = 100
    print(f"Guess the number: the computer will have a number and you are gonna guest it.\nYou have {intentos} tries to guess")
    random_number = create_a_number(min,max)
    guess = player_guess(min,max)
    while True:
        min,max = evaluation(guess,random_number,intentos,min,max)
        if min == 0 or max == 0:
            break
        intentos -= 1
        print(f"you have {intentos} tries left")
        if intentos == 0:
            print(f"you Lose, it was {random_number}")
            break
        guess = player_guess(min,max)

def adivinador():
    intentos = 7
    min = 1
    max = 100
    print(f'Guess the number: you have a number from 1 to 100 and the computer will try to guess it in {intentos} tries')
    print("hold your number in your head...")
    while True:
        random_number = create_a_number(min,max)
        try:
            respuesta = str(input(f'is {random_number} your number?:\nif it is correct(c)\nif it is lower(me)\nif it is greater(ma)\n '))
            if respuesta != 'me' and respuesta != 'ma' and respuesta != 'c':
                raise Exception
            else:
                min,max = computer_guess(respuesta,min,max,random_number)
                if min == 0 or max == 0:
                    print(f'in {intentos} tries left')
                    break
                intentos -= 1
                if intentos == 0:
                    print(f"i lose")
                    break
        except:
            print('invalid input')

def computer_guess(respuesta,min,max,random_number):
    if respuesta == 'c':
        print('i win!')
        return 0,0

    if respuesta == 'me':
        max = random_number - 1
    if respuesta == 'ma':
        min = random_number + 1

    return min,max

def replay():
    while True:
        try:
            respuesta = input("Wanna play again?(y/n)")
            if respuesta == 'y':
                interface()
            if respuesta == 'n':
                print("goodbye")
                break
            else:
                raise Exception
        except:
            print('invalid input:')

if __name__ == '__main__':

    interface()
    replay()