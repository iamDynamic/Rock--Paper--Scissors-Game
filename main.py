import random

RPS = {
    "rock" : 0,
    "paper" : 1,
    "scissors" : 2
}
Player = input()

ComputerChoice = random.choice(list(RPS.keys()))


if ComputerChoice == "rock" and Player == "rock" or ComputerChoice == "paper" and Player == "paper" or ComputerChoice == "scissors" and Player == "scissors":
  print("you are draw")
  print(ComputerChoice)
  
  # computer win coditions
if ComputerChoice == "rock" and Player == "scissors" or ComputerChoice == "scissors" and Player == "paper" or ComputerChoice == "paper" and Player == "rock":
  print("you lose")
  print(ComputerChoice)
if Player == "rock" and ComputerChoice == "scissors" or Player == "scissors" and ComputerChoice == "paper" or Player == "paper" and ComputerChoice == "rock":
  print("you win")
  print(ComputerChoice)

