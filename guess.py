import random

def play():
    secret = random.randint(1, 100)
    attempts = 0
    print("\n🎮 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.\n")

    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < secret:
            print("Too low! Try higher.\n")
        elif guess > secret:
            print("Too high! Try lower.\n")
        else:
            print(f"\nYou got it in {attempts} attempt{'s' if attempts != 1 else ''}!")
            break

    play_again = input("\nPlay again? (y/n): ").strip().lower()
    if play_again == 'y':
        play()
    else:
        print("Thanks for playing!\n")

play()
