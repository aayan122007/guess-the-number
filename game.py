import random

def play_game():
    number = random.randint(1, 100)
    guess = None
    tries = 0

    print("🎮 Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 100.")

    while guess != number:
        try:
            guess = int(input("Enter your guess: "))
            tries += 1
            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"🎉 Correct! You guessed it in {tries} tries.")
        except ValueError:
            print("❗ Please enter a valid number.")

    return tries

def save_score(tries):
    with open("score.txt", "a") as f:
        f.write(f"You guessed the number in {tries} tries.\n")

def main():
    while True:
        tries = play_game()
        save_score(tries)

        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing! Goodbye 👋")
            break

if __name__ == "__main__":
    main()
