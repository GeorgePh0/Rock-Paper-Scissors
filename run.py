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
    print("Welcome to my Rock Paper Scissor game. \n")
    player = " "
    while True:
        player = input("Please enter your name: ").strip()
        if player.isalpha() is not True:
            print("\nError: Please enter letters only\n")
            continue
        else:
            clear()
            print(f'Hi {player}, welcome to my game of rock, paper, scissors.')
            break


def rules():
    """
    Function to ask if the user wants to read the rules
    or go straight into the game
    """
    rules = input("\nTo see the rules press 'y', else press 'n' to continue: "
                  ).strip().lower()
    while True:
        if rules not in ["y", "n"]:
            rules = input("\nInvalid. \
would you like the rules 'y' for yes or 'n' for no: ").strip().lower()
            continue
        else:
            if rules == 'y':
                clear()
                print("The rules of Rock, Paper, Scissors is simple.\n"
                      "Rock beats Scissors\n"
                      "Scissors beats Paper\n"
                      "Paper beats Rock\n")
                break
            else:
                clear()
                break


def player_choice():
    """
    Function to get players choice and to check if the choice is valid.
    """
    while True:
        try:
            player_option = input("please choose rock, paper or scissors : "
                                  ).strip().lower()
            if player_option not in options:
                raise ValueError()
        except ValueError:
            print("\nNot valiad answer.\n")
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
    global player_score, computer_score
    while True:
        if player_option == computer_option:
            print("That is a tie, choose again!\n")
        elif (player_option == "rock" and computer_option == "scissors") or \
             (player_option == "paper" and computer_option == "rock") or \
             (player_option == "scissors" and computer_option == "paper"):
            print("you win \n")
            player_score += 1
        else:
            print("computer wins \n")
            computer_score += 1
        break


def game_over():
    """
    Function to check if user or computer
    has won twice and to then end the game.
    """
    return player_score == 2 or computer_score == 2


def restart():
    """
    Function to ask the user
    if they would like to play again or to end the game.
    """
    while True:
        restart_or_end = input("Would you like to play again? y or n: "
                               ).strip().lower()
        if restart_or_end == 'y':
            clear()
            start_game()
        elif restart_or_end == 'n':
            print("\nThank you for playing.\n")
            exit()
        else:
            print("\nInvalid. \
Please choose either 'y' for yes or 'n' for no: \n")


def restart_score():
    """
    Function to restart the scores to 0
    """
    global player_score, computer_score
    player_score = 0
    computer_score = 0


def start_game():
    """
    Function to start the game
    """
    while True:
        player_option = player_choice()
        computer_option = computer_choice()

        clear()

        print("3")
        time.sleep(0.75)
        print("2")
        time.sleep(0.75)
        print("1")
        time.sleep(0.75)
        print("show")
        time.sleep(0.2)
        print(f"\nYou chose {player_option}, \
computer chose {computer_option}.\n")

        determine_winner(player_option, computer_option)

        if game_over():
            print("Game Over\n")
            restart_score()
            restart()
            break


def main():
    """
    Main function to call all game functions
    """
    welcome()
    rules()
    start_game()


if __name__ == "__main__":
    main()
