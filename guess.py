import random
import json
import os

SCORES_FILE = "scores.json"

DIFFICULTIES = {
    "1": ("Easy",   1, 100, 10),
    "2": ("Medium", 1, 100, 7),
    "3": ("Hard",   1, 100, 5),
}

def load_scores():
    if os.path.exists(SCORES_FILE):
        with open(SCORES_FILE, "r") as f:
            return json.load(f)
    return []

def save_score(name, difficulty, attempts, max_attempts):
    scores = load_scores()
    scores.append({
        "name": name,
        "difficulty": difficulty,
        "attempts": attempts,
        "max_attempts": max_attempts,
    })
    scores.sort(key=lambda x: x["attempts"])
    with open(SCORES_FILE, "w") as f:
        json.dump(scores, f, indent=2)

def show_leaderboard():
    scores = load_scores()
    if not scores:
        print("\nNo scores yet!\n")
        return
    print("\n--- Leaderboard (best scores first) ---")
    for i, s in enumerate(scores[:10], 1):
        print(f"  {i}. {s['name']} | {s['difficulty']} | {s['attempts']} guess{'es' if s['attempts'] != 1 else ''}")
    print()

def choose_difficulty():
    print("\nChoose difficulty:")
    print("  1. Easy   (10 guesses)")
    print("  2. Medium (7 guesses)")
    print("  3. Hard   (5 guesses)")
    while True:
        choice = input("Enter 1, 2, or 3: ").strip()
        if choice in DIFFICULTIES:
            return DIFFICULTIES[choice]
        print("Please enter 1, 2, or 3.")

def play(name):
    diff_name, low, high, max_attempts = choose_difficulty()
    secret = random.randint(low, high)
    attempts = 0

    print(f"\nOK {name}, I'm thinking of a number between {low} and {high}.")
    print(f"You have {max_attempts} guesses. Good luck!\n")

    while attempts < max_attempts:
        remaining = max_attempts - attempts
        try:
            guess = int(input(f"Guess ({remaining} left): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < secret:
            print("Too low!\n")
        elif guess > secret:
            print("Too high!\n")
        else:
            print(f"\nYou got it in {attempts} guess{'es' if attempts != 1 else ''}!")
            save_score(name, diff_name, attempts, max_attempts)
            show_leaderboard()
            return

    print(f"\nOut of guesses! The number was {secret}.")

def reverse_mode(name):
    print(f"\nOK {name}, think of a number between 1 and 100.")
    input("Press Enter when you're ready...")

    low, high = 1, 100
    attempts = 0

    while True:
        guess = (low + high) // 2
        attempts += 1
        print(f"\nMy guess: {guess}")
        print("  h = too high   l = too low   c = correct")

        while True:
            response = input("Your response: ").strip().lower()
            if response in ("h", "l", "c"):
                break
            print("Please enter h, l, or c.")

        if response == "c":
            print(f"\nGot it in {attempts} guess{'es' if attempts != 1 else ''}! Binary search wins again.")
            break
        elif response == "h":
            high = guess - 1
        else:
            low = guess + 1

        if low > high:
            print("\nHmm, something doesn't add up — did I get a wrong answer? Try again!")
            break


def main():
    print("\n🎮 Number Guessing Game")
    print("=======================")
    name = input("Enter your name: ").strip() or "Player"

    while True:
        print("\nWhat would you like to do?")
        print("  1. Play (you guess)")
        print("  2. Reverse mode (computer guesses)")
        print("  3. View leaderboard")
        print("  4. Quit")
        choice = input("Enter 1, 2, 3, or 4: ").strip()
        if choice == "1":
            play(name)
        elif choice == "2":
            reverse_mode(name)
        elif choice == "3":
            show_leaderboard()
        elif choice == "4":
            print(f"\nSee you next time, {name}!\n")
            break
        else:
            print("Please enter 1, 2, 3, or 4.")

main()
