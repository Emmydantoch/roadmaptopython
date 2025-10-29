# Rock Paper Scissors
# value = input("please enter a value")

# print(value)

import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


# print(RPS(2))
# print(RPS.ROCK)
# print(RPS["ROCK"])
# print(RPS.ROCK.value)
# sys.exit("Exiting the program")

print("")
playerchoice = input(
    "Please enter your choice.......\n1 for rock, \n2 for paper, or \n3 for scissors:\n\n "
)
player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("Invalid choice, enter 1, 2 or 3 please try again")

computerchoice = random.choice("123")
computer = int(computerchoice)

# print("")
# print("You chose" + str(RPS(player)).replace("RPS.", "") + ".")
# print("python chose" + str(RPS(player)).replace("RPS.", "") + ".")
# print("")

if player == computer:
    print("It's a tie!")
elif player == 1 and computer == 2:
    print("python wins!")
elif player == 1 and computer == 3:
    print("You win!")
elif player == 2 and computer == 1:
    print("You win!")
elif player == 2 and computer == 3:
    print("python wins!")
elif player == 3 and computer == 1:
    print("python wins!")
elif player == 3 and computer == 2:
    print("You win!")
