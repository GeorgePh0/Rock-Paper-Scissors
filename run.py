# selects a random option
import random

def welcome():
    """
    Function prints a welcome message and asks the user
    if they want to learn the rules or go into the game
    """
    print("Welcome to Rock Paper Scissor. \n"
    "If you want to learn the rules of the game then press 'y' \n"
    "If you want to go straight into the game then press 'n' \n")
    rules = input("")
    if rules == 'y':
        print("Here are the rules")
    else:
        print("Go into the game")


welcome()

