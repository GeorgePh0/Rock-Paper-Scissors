# selects a random option
import random

def welcome():
    """
    Function prints a welcome message and asks the user
    if they want to learn the rules or go into the game
    """
    print("Welcome to Rock Paper Scissor. \n")
    player = " "
    while True:
        player = input("Please enter your name: ")
        if player.isalpha() is not True:
            print("Error: Please enter letters only")
            continue
        else:
            print(f'Hi {player}, welcome to the game')
            return player


def rules():
    rules = input("If you would like to see the rules to the game press 'y'. \n"
    "If you would like to go into the game then press 'n'")
    print(rules)
    if rules == 'y':
        print("rules")
    elif rules == 'n':
        print("game")
    else:
        print("invalid")

welcome()
rules()

