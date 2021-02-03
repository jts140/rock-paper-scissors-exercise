# game.py
import random

print("Rock, Paper, Scissors, Shoot!")

print("-------------------")

print("Welcome 'Player One' to my Rock-Paper-Scissors game...")

#asking user inputs

print("-------------------")

user_choice = input("Please choose either 'rock', 'paper', or 'scissors'")

print("You chose:", user_choice)



#simulating a computer input
foo = ["rock","paper", "scissors"]
computer_choice = random.choice(foo)

print("The computer chose:", computer_choice)


print("-------------------")

# determining who won


if user_choice == computer_choice:
        print("It's tie!")
   elif user_choice == "paper" and computer_choice == "rock":
        print("You win! Congrats")
    elif user_choice == "paper" and computer_choice == "scissors":
        print("Oh! The computer won, that's ok!")
    elif user_choice == "rock" and computer_choice == "paper":
        print("Oh! The computer won, that's ok!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win! Congrats")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win! Congrats")
    elif user_choice == "scissors" and computer_choice == "rock":
        print("Oh! The computer won, that's ok!")

print("-------------------")

print("Thanks for playing. Please play again!")