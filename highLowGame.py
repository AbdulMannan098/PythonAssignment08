import random

def get_valid_input():
    while True:
        guess = input(f"Your number is {player_number}. Do you think it is higher or lower than the computer's number? (Type 'higher' or 'lower'): ").lower()
        if guess in ['higher', 'lower']:
            return guess
        else:
            print("Invalid input! Please type 'higher' or 'lower'.")

NUM_ROUNDS = 5
score = 0

for round_number in range(1, NUM_ROUNDS + 1):
    player_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)

    print(f"\n--- Round {round_number} ---")
    user_guess = get_valid_input()

    if (player_number > computer_number and user_guess == "higher") or (player_number < computer_number and user_guess == "lower"):
        print("Correct! You guessed right.")
        score += 1
    else:
        print(f"Wrong! The computer's number was {computer_number}.")

    print(f"Your score so far: {score}")

print(f"\nGame over! Your final score is {score} out of {NUM_ROUNDS}.")

if score == NUM_ROUNDS:
    print("Amazing! You got a perfect score!")
elif score > NUM_ROUNDS // 2:
    print("Great job! You scored more than half.")
else:
    print("Better luck next time! You scored less than half.")
