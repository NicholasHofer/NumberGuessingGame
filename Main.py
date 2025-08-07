import random

class Difficulty:
    def __init__(self, number):
        if number == 1:
            self.difficulty_name = "Easy"
            self.guesses = 10
        elif number == 2:
            self.difficulty_name = "Medium"
            self.guesses = 5
        elif number == 3:
            self.difficulty_name = "Hard"
            self.guesses = 3
        else:
            print("Invalid difficulty number. Please choose either 1, 2, or 3.")

def start_game():
    print('Please select the difficulty level:')
    print('1. Easy (10 changes)')
    print('2. Medium (5 chances)')
    print('3. Hard (3 chances)')
    
    # Force user to choose a valid difficulty (1, 2, or 3)
    while True:
        try:
            n = int(input('\nEnter your choice: '))
            if n in (1, 2, 3):
                break
            else:
                print('Invalid input. Please enter either 1, 2, or 3.')
        except Exception:
            print('Invalid input. You must enter a number.')

    difficulty = Difficulty(int(n))

    print(f"\nGreat! You have selected the {difficulty.difficulty_name} difficulty. You will have {difficulty.guesses} guesses.")
    print("Let's start the game! I'm thinking of a number between 1 and 100...\n")

    # Begin game
    i = random.randint(1, 100)
    max_guesses = difficulty.guesses #10
    current_guess = max_guesses 
    winner = False
    while current_guess > 0:
        try:
            guess = int(input(f"Enter your guess: "))
            if guess == i:
                winner = True
                break
            else:
                current_guess -= 1
                print(f"Try again! {current_guess} guesses left.")
        except Exception:
            print("Invalid input. Please try again.")

    if winner == True:
        rounds = (max_guesses - current_guess) + 1
        print(f"\nCorrect! You guessed my number in {rounds} rounds!\n")
    else:
        print(f"\nBetter luck next time. My number was {i}. Thanks for playing!\n")

if __name__ == "__main__":
    start_game()