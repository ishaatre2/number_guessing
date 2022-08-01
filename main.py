#Number Guessing Game Objectives:
import random
from art import logo

print(logo)

EASY_TURNS = 10
HARD_TURNS = 5


#check answer
def check_answer(user_guess, answer, turns):
  """checks if the answer is correct. returns the number of turns remaining"""
  if user_guess > answer:
      print("Too high")
      return turns - 1
  elif user_guess < answer:
      print("Too Low")
      return turns - 1
  else:
      print(f"You got it, the correct answer is {answer}")


def set_difficulty():
  level = input("Choose the level of difficulty, type easy or hard")
  if level == "easy":
    return EASY_TURNS
  else:
    return HARD_TURNS


# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
def game():
  print("Welcome to the number guessing game.")
  print("I am thinking of a number between 1 to 100.")
  answer = random.randint(1, 100)
  

  turns = set_difficulty()

  user_guess = 0
  while user_guess != answer:
    print(f"You have {turns} turns left to guess the correct answer.")
    user_guess = int(input("Make a guess:"))
    turns = check_answer(user_guess, answer, turns)
    if turns == 0:
      return


# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.

# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

#step 1--> split the game into parts
#two parts are the turns and checking the games
game()
