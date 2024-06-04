# -------------------#
# //* A rock ,paper ,scissor game in python
import random

player = None
# List of possible choices
choices = ["rock", "paper", "scissors"]

while True:
    # Computer's choice
    computer = random.choice(choices)

    player = input("Enter your choice (rock, paper, scissors): \n-->").lower()
    if player not in choices:
        # Player's choice
        player = input("Enter your choice (rock, paper, scissors): \n-->").lower()
    else:
        print(f"Computer has Chosen :{computer}")
        print(f"You have chosen :{player}")

        if player == computer:
            print("This is a tie!!!")
        elif player == "rock":
            if computer == "paper":
                print("Better luck next time!")
            else:  # computer == "scissors"
                print("Congratulations!\n You won the game!")
        elif player == "paper":
            if computer == "rock":
                print("Congratulations!\n You won the game!")
            else:  # computer == "scissors"
                print("Better luck next time!")
        elif player == "scissors":
            if computer == "rock":
                print("Better luck next time!")
            else:  # computer == "paper"
                print("Congratulations!\n You won the game!")

    # asking if player wants to continue
    play_again = input(
        "Scissors snips paper, paper covers rock, rock crushes scissors.\nwanna play again(yes/no)?\n"
    ).lower()
    if play_again != "yes":
        break
# otherwise quitting this game
print("Thanks for playing.\nCatch you later!")
