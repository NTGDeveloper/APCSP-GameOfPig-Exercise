# The Game of Pig

# Init variables and also dependencies
import random

dice_1 = 0
dice_2 = 0
player1_score = 0
player2_score = 0
score = 0
round = 0
player = 0
computer_score = 0


# Main function
def roll_dice(round, score, verbose):
  choice = "roll"
  round_score = 0
  roll_count = 0
  while choice == "roll":
    roll_count += 1
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    if verbose == "Y" or verbose == "y":
      print("\nRoll #" + str(roll_count))
      print("Dice 1 = " + str(dice_1) + "\nDice 2 = " + str(dice_2))
    if dice_1 == 1 and dice_2 == 1:
      if player != "computer":
        print("\nYou rolled SNAKEEYES! \nYour total score is now reset.\n")
        input("Press [Enter] to continue ")
      round_score = 0
      score = 0
      choice = "snakeeyes"
      break
    elif dice_1 == 1 or dice_2 == 1:
      if player != "computer":
        print(
          "\nOne of the dice is 1! \nYour score for this round is now reset.")
      round_score = 0
    else:
      round_score += (dice_1 + dice_2)
      print("Round Score: " + str(round_score))

    if player != "computer":
      choice = input("\nWould you like to roll or bank? ")
      if choice == "bank":
        break

    elif player == "computer":
      if round_score >= 20:
        choice = "bank"
      else:
        choice = "roll"

  score += round_score
  return score


# Actual Program Part
print("Welcome to the Game of Pig! (whatever that is)\nWIP\n\n")
game_choice = input("Computer (C) or Two-Players (P)? ")
if game_choice == "P" or game_choice == "p":
  verbose = "Y"
  while player1_score < 100 and player2_score < 100:
    round += 1
    print("\n\nPlayer 1's Turn " + str(round))
    player1_score = roll_dice(round, player1_score, verbose)
    print("\nEnd of Round Stats:")
    print("Player 1 Score: " + str(player1_score))
    print("Player 2 Score: " + str(player2_score))
    if player1_score >= 100:
      break
    print("\n\nPlayer 2's Turn " + str(round))
    player2_score = roll_dice(round, player2_score, verbose)
    if player2_score >= 100:
      break
    print("\nEnd of Round Stats:")
    print("Player 1 Score: " + str(player1_score))
    print("Player 2 Score: " + str(player2_score))
elif game_choice == "c" or game_choice == "C":
  verbose = input("Would you like to see the AI's dice? (Y or N) ")
  while player1_score < 100 and computer_score < 100:
    round += 1
    player = 1
    print("\n\nPlayer's Turn " + str(round))
    player1_score = roll_dice(round, player1_score, verbose)
    print("\nEnd of Round Stats:")
    print("Player Score: " + str(player1_score))
    print("Computer Score: " + str(computer_score))
    if player1_score >= 100:
      break
    print("\n\nComputer's Turn " + str(round))
    player = "computer"
    computer_score = roll_dice(round, computer_score, verbose)
    if computer_score >= 100:
      break
    print("\nEnd of Round Stats:")
    print("Player Score: " + str(player1_score))
    print("Computer Score: " + str(computer_score))
if player1_score >= 100:
  print("\n\n\nPlayer 1 Wins!\n")
  print("\nWinning Score: " + str(player1_score))
  print("Loosing Score: " + str(player2_score))
elif player2_score >= 100:
  print("\n\n\nPlayer 2 Wins!\n")
  print("\nWinning Score: " + str(player2_score))
  print("Loosing Score: " + str(player1_score))
elif computer_score >= 100:
  print("\n\n\nComputer Wins!\n")
  print("\nComputer Score: " + str(computer_score))
  print("Player Score: " + str(player1_score))
