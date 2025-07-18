import random
from user_guess_selection import difficulty_selection, displayGameMenu

def main():

    try:
        displayGameMenu()
        chances = difficulty_selection()
        tries = chances
        guess = random.randint(1, 100)

        while chances > 0:
            print(guess)
            user_guess = int(input("Enter your guess: "))
            
            if user_guess > guess:
                chances -= 1
                print(f"Incorrect! The number is less than {user_guess}.")
            elif user_guess < guess:
                chances -= 1
                print(f"Incorrect! The number is greater than {user_guess}.")
            else:
                chances -= 1
                print(f"Congratulations! You guessed the correct number in {tries - chances} attempt(s).")
                return

        if not chances:
            print("Game over\nGoodbye!")
    except TypeError:
        print("Please enter a number (1, 2, or 3).")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()