def displayGameMenu():
    print("Welcome to the Number Guessing Game!\n"
          "I'm thinking of a number between 1 and 100.\n"
          "You have 5 chances to guess the correct number.\n"
          "\nPlease select the difficulty level:\n"
          "1. Easy (10 chances)\n"
          "2. Medium (5 chances)\n"
          "3. Hard (3 chances)\n")

def difficulty_selection():

    difficulty_level = {1: "Easy", 2: "Medium", 3: "Hard"}
    chances = [10, 5, 3]

    try:
        user_difficulty = int(input("Enter your choice: "))
        match user_difficulty:
            case 1:
                difficulty_level = difficulty_level[1]
            case 2:
                difficulty_level = difficulty_level[2]
            case 3:
                difficulty_level = difficulty_level[3]
            case _:
                raise

        if isinstance(difficulty_level, str):
            print(f"\nGreat! You have selected the {difficulty_level} difficulty level.\n"
                f"Let's start the game!\n")
            return chances[user_difficulty - 1]
    except:
        print("Please enter a number (1, 2, or 3).")
