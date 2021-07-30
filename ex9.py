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

if __name__ == '__main__':
    intentos = 7
    min = 1
    max = 100
    print(f"Gues the number: the computer will have a number and you are gonna guest it.\nYou have {intentos} to guess")
    random_number = create_a_number(min,max)
    guess = player_guess(min,max)
    while True:
        min,max = evaluation(guess,random_number,intentos,min,max)
        if min == 0 or max == 0:
            break
        intentos -= 1
        if intentos == 0:
            print(f"you Lose, it was {random_number}")
            break
        guess = player_guess(min,max)
    print("Wanna play again?")
    

# this part does not work....yet
class Interface():

    def __init__(self):
        self.game = Game()
        self.intentos = 7

class Game():

    def __init__(self):
        self.is_playing = True
        self.min = 1
        self.max = 100
        self.num = 0


class Adivina():

    def __init__(self):
        pass

class Adivinador():
    pass