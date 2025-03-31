# Kennedy Watson
# SCIS 111-113
# Dice Simulator
# 11.24.24
"""The purpose of this is to: Display a menu to either play a dice game
or simulate multiple games, track outcomes using dictionaries, and calculate/display counts
and percentages for each die face.
"""
import random

def play_individual_game():
# ends before 7 because dice are 6 sides
# use for loop (range)
    die1_counts = {i: 0 for i in range(1, 7)}
    die2_counts = {i: 0 for i in range(1, 7)}
    total_rolls = 0
# prompt player to roll dice
    while True:
        play = input("Play dice? (yes/no): ").strip().lower()
        if play == 'no':
            break
        elif play == 'yes':
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            print(f"Die 1 is: {die1}")
            print(f"Die 2 is: {die2}")
            
            die1_counts[die1] += 1
            die2_counts[die2] += 1
            total_rolls += 1
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

    die1_percentages = {key: round((value / total_rolls) * 100, 2) for key, value in die1_counts.items()}
    die2_percentages = {key: round((value / total_rolls) * 100, 2) for key, value in die2_counts.items()}
# display results
    print("\nDie 1 History:", die1_counts)
    print("Die 2 History:", die2_counts)
    print("The % of times Die 1 landed on a given value:", die1_percentages)
    print("The % of times Die 2 landed on a given value:", die2_percentages)

def simulate_games():
    die1_counts = {i: 0 for i in range(1, 7)}
    die2_counts = {i: 0 for i in range(1, 7)}

    try:
        num_games = int(input("Enter the number of games you would like to simulate: "))
        if num_games <= 0:
            print("Please enter a positive integer.")
            return

        for _ in range(num_games):
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            die1_counts[die1] += 1
            die2_counts[die2] += 1

        die1_percentages = {key: round((value / num_games) * 100, 2) for key, value in die1_counts.items()}
        die2_percentages = {key: round((value / num_games) * 100, 2) for key, value in die2_counts.items()}
        
        print("\nDie 1 History:", die1_counts)
        print("Die 2 History:", die2_counts)
        print("The % of times Die 1 landed on a given value:", die1_percentages)
        print("The % of times Die 2 landed on a given value:", die2_percentages)

    except ValueError:
        print("Invalid input. Please enter an integer.")

def main():
    print("Welcome to the Dice Simulation Program!")
    while True:
        print("\nMenu:")
        print("1. Play Individual Game of Dice")
        print("2. Simulate Multiple Dice Games")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            play_individual_game()
        elif choice == '2':
            simulate_games()
        elif choice == '3':
            print("Bye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
