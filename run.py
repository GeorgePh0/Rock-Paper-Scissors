# selects a random option
import random
# can set a timer
import time
# clears terminal
import os


# constant with list of options for the player to choose
options = ["rock", "paper", "scissors"]


def clear():
    """
    Function to clear the terminal
    """
    os.system('clear')

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
    rules = input("\n If you would like to see the rules to the game press 'y'. \n"
    "If you would like to go into the game then press 'n' \n")
    print(rules)
    while True:
        if rules not in ["y", "n"]:
            rules = input("Not valid answer. would you like the rules Y / N \n")
            continue
        else:
            if rules == 'y':
                clear()
                print("The rules of Rock, Paper, Scissors is simple. \n"
                "Rock beats Scissors \n"
                "Scissors beats Paper \n"
                "Paper beats Rock \n")
            else:
                clear()
                break


def player_choice():
    """
    Function to get players choice and to check if the choice is valid.
    """
    while True:
        try:
            player_option = input("please choose rock, paper or scissors : ")
            if player_option not in options:
                raise ValueError()
        except ValueError:
            print("Not valiad answer. Please choose rock, paper or scissors : ")
        else:
            return player_option


def start_game(player_option):
    computer_option = random.choice(options)
    print("3")
    time.sleep(0.75)
    print("2")
    time.sleep(0.75)
    print("1")
    time.sleep(0.75)
    print("show")
    time.sleep(0.1)
    print(player_option)
    # print(f"\nYou chose {player_option}, computer chose {computer_option}.\n")


def main():
    welcome()
    rules()
    player_option = player_choice()
    start_game(player_option)

if __name__ == "__main__":
    main()