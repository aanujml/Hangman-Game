import random
def play_hangman():
    words = ["python", "developer", "sequence", "variable", "function"]
    print("--- Welcome to Hangman! ---")

    # 1. Outer Loop: Handles restarting the game
    while True:
        # Reset game state variables for a brand new match
        secret_word = random.choice(words)
        guessed_word = ["_"] * len(secret_word)
        attempts_left = 6
        guessed_letters = set()

        # 2. Inner Loop: The active match loop
        while attempts_left > 0 and "_" in guessed_word:
            print(f"\nWord to guess: {' '.join(guessed_word)}")
            print(f"Attempts left: {attempts_left}")
            print(
                f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}"
            )

            guess = input("Guess a letter: ").lower().strip()

            # Input Validation
            if len(guess) != 1 or not guess.isalpha():
                print(
                    "Invalid input. Please enter a single alphabetical letter."
                )
                continue

            if guess in guessed_letters:
                print(f"You already guessed '{guess}'. Try a different letter.")
                continue

            guessed_letters.add(guess)

            # Check guess matching
            if guess in secret_word:
                print(f"Good job! '{guess}' is in the word.")
                for index, letter in enumerate(secret_word):
                    if letter == guess:
                        guessed_word[index] = guess
            else:
                print(f"Sorry, '{guess}' is not in the word.")
                attempts_left -= 1

        # 3. Match End Evaluation
        print("\n------------------------")
        if "_" not in guessed_word:
            print(f"Congratulations! You won! The word was: {secret_word}")
        else:
            print(
                f"Game Over! You ran out of attempts. The word was: {secret_word}"
            )
        print("------------------------")

        # 4. Play Again Prompt
        play_again = (
            input("Would you like to play again? (y/n): ").lower().strip()
        )

        if play_again != "y" and play_again != "yes":
            print("\nThanks for playing! Goodbye.")
            break  # Breaks the outer loop and exits the function


if __name__ == "__main__":
    play_hangman()