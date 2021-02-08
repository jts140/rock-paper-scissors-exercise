# game.py
import random

print("Rock, Paper, Scissors, Shoot!")

print("-------------------")

print("Welcome 'Player One' to my Rock-Paper-Scissors game...")

#asking user inputs
print("-------------------")

user_choice = input("Please choose either 'rock', 'paper', or 'scissors'")
print("You chose:", user_choice)

# data validation for User
foo = ["rock","paper", "scissors"]
if user_choice  not in foo:
    print("Please chose a vaild option (rock, paper, or scissors) and run the program again")
    exit()

#simulating a computer input
computer_choice = random.choice(foo)

print("The computer chose:", computer_choice)

print("-------------------")

# determining who won (modified from Slack)
if user_choice == "rock":
    if computer_choice == "rock":
        print("Oh, it's a tie.")
    elif computer_choice == "paper":
        print("Oh, the computer won. It's ok.")
    elif computer_choice == "scissors":
        print("Oh, you won! Nice job.")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("Oh, you won! Nice job.")
    elif computer_choice == "paper":
        print("Oh, it's a tie.")
    elif computer_choice == "scissors":
        print("Oh, the computer won. It's ok.")
elif user_choice == "scissors":
    if computer_choice == "rock":
        print("Oh, the computer won. It's ok.")
    elif computer_choice == "paper":
        print("Oh, you won! Nice job.")
    elif computer_choice == "scissors":
        print("Oh, it's a tie.")
else:
    print("OOPS SOMETHING WENT WRONG.")

print("-------------------")

print("Thanks for playing. Please play again!")