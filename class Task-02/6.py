import random

high_scores = []

def play_game():

    print("===== NUMBER GUESSING GAME =====")
    print("Choose Difficulty:")
    print("1. Easy (1-50, 10 tries)")
    print("2. Medium (1-100, 7 tries)")
    print("3. Hard (1-500, 9 tries)")

    choice = input("Enter choice (1/2/3): ")

    # Difficulty settings
    if choice == "1":
        limit = 50
        max_attempts = 10
    elif choice == "3":
        limit = 500
        max_attempts = 9
    else:
        limit = 100
        max_attempts = 7

    secret = random.randint(1, limit)
    attempts = 0
    guessed = False

    print(f"\nGuess a number between 1 and {limit}")

    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == secret:
            print("Correct!")
            guessed = True
            break
        elif guess > secret:
            print("Too high!")
        else:
            print("Too low!")

    if not guessed:
        print("Game Over! Number was:", secret)

    # Stats
    efficiency = ((max_attempts - attempts + 1) / max_attempts) * 100

    print("\n===== GAME STATS =====")
    print("Attempts used:", attempts)
    print(f"Efficiency: {efficiency:.2f}%")

    # Save high score (less attempts = better)
    high_scores.append(attempts)
    high_scores.sort()
    del high_scores[5:]   # keep top 5 only

    print("\n===== HIGH SCORES (Top 5) =====")
    for i, score in enumerate(high_scores, start=1):
        print(f"{i}. {score} attempts")


# Run game
play_game()