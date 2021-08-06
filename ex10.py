"""Design a program with Python using list. 
The program will ask from the user to enter the players score and after the it will show the highest score"""

class InvalidInteger(Exception):
    def __init__(self, message):
        print(message)

def amount_of_players():
    while True:
        try:
            players = int(input("enter the amount of players to score: "))
            if players <= 0:
                raise InvalidInteger("must be a positive number")
            return players

        except:
            print('invalid input')

def list_of_score(players):
    score_list= []
    count = 1
    while (players+1) != count:
        try:
            score = float(input(f"enter the score of player {count}: "))
            if score < 0:
                raise InvalidInteger("must be a positive number")
            count += 1
            score_list.append(score)


        except:
            print('invalid input')
    return score_list

def sorted_list(list_score):
    score_sorted = sorted(list_score,reverse=True)
    for elements in range(len(list_score)):
        if list_score[elements] == score_sorted[0]:
            print(f'highest score: Player {elements+1}: {score_sorted[0]}')



def main():
    players = amount_of_players()
    list_score = list_of_score(players)
    sorted_list(list_score)



if __name__ == '__main__':
    main()
