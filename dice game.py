# Troy and Eddie
# Chicago dice game

import random

def create():
    print("Welcome to Chicago! There are 11 rounds in this game numbered 2-12.You have two dice.If you roll the round number on that round, you earn 5 points! Gather as many points at the end of 11 rounds!")
    print("Press Enter to start the game.")
    input()


def dice_roll():
    roll = random.randint(2, 12)
    return roll


def play_game():
   round1 = 2
   round2 = 3
   round3 = 4
   round4 = 5
   round5 = 6
   round6 = 7
   round7 = 8
   round8 = 9
   round9 = 10
   round10 = 11
   round11 = 12
   points = 0
   roll = dice_roll()
   print ("Round 1. Roll the dice!")
   print(f"You rolled {roll}")
   if roll == round1:
       print("You have earned 5 points.")
       points = points + 5
   else:
       print("You earned no points on this round.")
   print(f"You have {points} points now!")
   input()
   print("Round 2. Roll the dice")
   roll
   print(f"You rolled {roll}")
   if roll == round2:
       print("You have earned earned 5 points")
       points = points + 5
   else:
       print("You earned no points on this round.")
   print(f"You have {points} points now!")
   input()
   print("Round 3. Roll the dice")
   dice_roll()
   print(f"You rolled {roll}")
   if roll == round3:
       print("You have earned earned 5 points")
       points = points + 5
   else:
       print("You earned no points on this round.")
   print(f"You have {points} points now!")
   input()
   print("Round 4. Roll the dice")
   print(f"You rolled {roll}")
   if roll == round4:
       print("You have earned earned 5 points")
       points = points + 5
   else:
       print("You earned no points on this round.")
   if points == 20:
       print("You have 20 points! You won the game!")
   print(f"You have {points} points now!")
   input()
   print("Round 5. Roll the dice")
   dice_roll()
   print(f"You rolled {roll}")
   if roll == round5:
       print("You have earned earned 5 points")
       points = points + 5
   else:
       print("You earned no points on this round.")
   print(f"You have {points} points now!")
   print("Round 6. Roll the dice")
   dice_roll()
   print(f"You rolled {roll}")
   if roll == round6:
       print("You have earned earned 5 points")
       points = points + 5
   else:
       print("You earned no points on this round.")
   if points == 20:
       print("You have 20 points! You won the game!")
   print(f"You have {points} points now!")
   input()
   print("Round 7. Roll the dice")
   dice_roll()
   print(f"You rolled {roll}")
   if roll == round7:
       print("You have earned earned 5 points")
       points = points + 5
   else:
       print("You earned no points on this round.")
   print(f"You have {points} points now!")
   if points == 20:
       print("You have 20 points! You won the game!")
   input()
   print("Round 8. Roll the dice")
   dice_roll()
   print(f"You rolled {roll}")
   if roll == round8:
       print("You have earned earned 5 points")
       points = points + 5
   else:
       print("You earned no points on this round.")
   print(f"You have {points} points now!")
   if points == 20:
       print("You have 20 points! You won the game!")
   input()
   print("Round 9. Roll the dice")
   dice_roll()
   print(f"You rolled {roll}")
   if roll == round9:
       print("You have earned earned 5 points")
       points = points + 5
   else:
       print("You earned no points on this round.")
   print(f"You have {points} points now!")
   if points == 20:
       print("You have 20 points! You won the game!")
   input()
   print("Round 10. Roll the dice")
   dice_roll()
   print(f"You rolled {roll}")
   if roll == round10:
       print("You have earned earned 5 points")
       points = points + 5
   else:
       print("You earned no points on this round.")
   print(f"You have {points} points now!")
   if points == 20:
       print("You have 20 points! You won the game!")
   input()
   print("Round 11. Roll the dice")
   dice_roll()
   print(f"You rolled {roll}")
   if roll == round11:
       print("You have earned earned 5 points")
       points = points + 5
   else:
       print("You earned no points on this round.")
   print(f"You have {points} points now!")
   if points == 20:
       print("You have 20 points! You won the game!")
   else:
       print("You didn't get 20 points. You lost.")
   print("Would you like to play again? Y or N?")
   decision = input()
   if decision == "Y":
       create()
       play_game()
   else:
       print("Game Over.")

create()
play_game()
