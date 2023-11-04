# selects a random option
import random
# can set a timer
import time
# clears terminal
import os


# constant with list of options for the player to choose
options = ["rock", "paper", "scissors"]
# variables to keep the count of the scores
player_score = 0
computer_score = 0


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
    """
    Function to ask if the user wants to read the rules
    or go straight into the game
    """
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


def computer_choice():
    """
    Function to get the computers choice between the options
    """
    computer_option = random.choice(options)
    return computer_option


def determine_winner(player_option, computer_option):
    """
    Function to find out the winner or if the player and computer
    had tied the game
    """
    while True:
        if player_option == computer_option:
            print("That is a tie, choose again and try and beat the computer!")
        elif (player_option == "rock" and computer_option == "scissors") or \
        (player_option == "paper" and computer_option == "rock") or \
        (player_option == "scissors" and computer_option == "paper"):
            print("you win")
        else:
            print("computer wins")
        break


def start_game(player_option, computer_option):
    """
    Function to start the game
    """
    print("3")
    time.sleep(0.75)
    print("2")
    time.sleep(0.75)
    print("1")
    time.sleep(0.75)
    print("show")
    time.sleep(0.2)
    print(f"\nYou chose {player_option}, computer chose {computer_option}.\n")
    determine_winner(player_option, computer_option)


def main():
    welcome()
    rules()
    player_option = player_choice()
    computer_option = computer_choice()
    start_game(player_option, computer_option)


if __name__ == "__main__":
    main()
