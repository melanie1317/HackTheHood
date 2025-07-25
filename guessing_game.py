#Guessing Game - Melanie, Calleigh, Oliver
    
import random

def generate_random_number():
    """Generate and return a random number between 1 and 100."""
    return random.randint(1, 100)


def get_user_guess():
    """Prompt the user to guess a number between 1 and 100. 
    Repeats until a valid integer in range is entered. 
    Returns the valid integer."""
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print(" Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def play_guessing_game():
    """ Play one round of the guessing game. 
    Generates a secret number and continues to prompt the user until they guess it.
    Provides feedback on whether the guess is too low, too high, or correct.
    Tracks the number of attempts."""
    secret_number = generate_random_number()
    attempts = 0

    print("\n I'm thinking of a number between 1 and 100.")
    
    while True:
        guess = get_user_guess()
        attempts += 1

        if guess < secret_number:
            print(" Too low. Try again.")
        elif guess > secret_number:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

def game_loop():
    """Controls the overall game loop.
    Allows the user to play multiple rounds until they choose to quit."""
    print("Welcome to the Number Guessing Game!")
    
    while True:
        play_guessing_game()
        play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if play_again not in ('yes', 'y'):
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    game_loop()