<<<<<<< HEAD
# Crete the number guessing game .
import random

secret = random.randint(1, 20)

print("Welcome to Guess the Number Game! ")
print("I'm thinking of a number between 1 and 20.")

while True:
    guess = int(input("Enter your guess: "))
=======
 import random

 secret = random.randint(1, 20)

 print("Welcome to Guess the Number Game! 🎲")
 print("I'm thinking of a number between 1 and 20.")

 while True:
     guess = int(input("Enter your guess: "))

    if guess == secret:
         print("🎉 Correct! You guessed the number.")
        break
    elif guess < secret:
         print("Too low! Try again.")
     else:
         print("Too high! Try again.")
>>>>>>> origin/main

    if guess == secret:
        print(" Correct! You guessed the number.")
        break
    elif guess < secret:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

#  create a simple rock, paper, scissors game.
import random

# Choices
choices = ["rock", "paper", "scissors"]

# Player input
player = input("Enter rock, paper, or scissors: ").lower()

# Computer random choice
computer = random.choice(choices)

print("You chose:", player)
print("Computer chose:", computer)

# Decide winner
if player == computer:
    print("It's a tie!")
elif (player == "rock" and computer == "scissors") or \
     (player == "scissors" and computer == "paper") or \
     (player == "paper" and computer == "rock"):
    print("You win! Yeahhhh!")
else:
    print("You lose! so Sad ")
