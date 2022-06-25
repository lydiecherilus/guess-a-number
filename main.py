# guess a number
import random 
from art_work import art, trophy

EASY_LEVEL = 10
INTERMEDIATE_LEVEL = 7
HARD_LEVEL = 5
print(art)


def difficulty_level():
    """set the difficulty level"""
    level_option = input('Please choose a difficulty level. Type "1" for easy, "2", "3" ')
    while level_option != "1" or level_option != "2" or level_option != "3":
        level_option = input('Please confirm difficulty level. Type "1" for easy, "2", "3" ')
        print("*** ***")
        if level_option == "1":
            return EASY_LEVEL
        elif level_option == "2":
            return INTERMEDIATE_LEVEL
        elif level_option == "3":
            return HARD_LEVEL
        else:
            print("Please enter a valid option")


def check_answer(guess, chosen_number, remaining_guess):
    """check user guess againt computer chosen number and return the number of remaining guesses"""
    if guess > chosen_number:
        print("Too high.")
        return remaining_guess - 1 
    elif guess < chosen_number:
        print("Too low.")
        return remaining_guess - 1
    else:
        print(f"the number is {chosen_number}, you win!")
        print(trophy)
        print("***** *****\n")
        restart = input('Type "yes" if you want to guess another number -- otherwise type "no". \n')
        if restart == "no":
            print("Goodbye")
            return
        elif restart == "yes":
            print(art)
            return game()


def game():
    print("Welcome to the Number Guessing Game")
    print("Guess a number from 1 to 100\n")
    chosen_number = random.randint(1, 100)
    remaining_guess = difficulty_level()
    
    # repeat the guessing if user did not guess the number
    guess = 0
    while guess != chosen_number:
        print(f"You have {remaining_guess} attempts remaining to guess the number.\n")

        # ask the user to guess a number
        guess = int(input("Make a guess: "))

        # track the number of guess remaining and reduce by 1 each time user guess wrong.
        remaining_guess = check_answer(guess, chosen_number, remaining_guess)
        if remaining_guess == 0:
            print(f"You have run out of guesses, you lose. \nThe number is {chosen_number}")
            print("***** *****\n")
            
            # give users option to play again or quit the game
            restart = input('Type "yes" if you want to guess another number -- otherwise type "no". \n')
            if restart == "no":
                print("Goodbye")
                return
            elif restart == "yes":
                print(art)
                return game()
        elif guess != chosen_number:
            print("Guess again.")
game()
