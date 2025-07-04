import random

guess = random.randint(1, 5)

print(f"Welcome to the Number Guessing Game!\n"
      f"I'm thinking of a number between 1 and 100.\n"
      f"You have 5 chances to guess the correct number.\n")

print(f"Please select the difficulty level:\n"
      f"1. Easy (10 chances)\n"
      f"2. Medium (5 chances)\n"
      f"3. Hard (3 chances)\n")

difficulty = input("Enter your choice: ")
chances = 0

match difficulty:
    case "1":
        level = "Easy"
        chances = 10
        print(f"Great! You have selected the {level} difficulty level.")
    case "2":
        level = "Medium"
        chances = 5
        print(f"Great! You have selected the {level} difficulty level.")
    case "3":
        level = "Hard"
        chances = 3
        print(f"\nGreat! You have selected the {level} difficulty level.\n"
              f"Let's start the game!\n")
    case _:
        print("Invalid value entered!")

user_guess = input("Enter your guess: ")


print(f"guess: ${guess}")
print(f"guess: ${difficulty}")
