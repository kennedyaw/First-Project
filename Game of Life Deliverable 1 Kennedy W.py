# Kennedy Watson
# Game of Life Project
# Deliverable 1
"""
- Game Setup
 Welcome player and explain the game
 "Welcome to the Game of Life! Your goal is to navigate through 100 spaces and manage your wealth."
 "You will start with $1000, and roll a die to move through the board. Good luck!"
 
Ask  player for their name and set the initial wealth.
Input: Player's name.
Set money/wealth to $1000.
"Hello [name], your starting wealth is $1000."

Career vs Education Path
Ask the player if they want to go to school or start a career
Input: Player's choice (school or career).
If "school", add $40,000 loan.
If "career", start immediately after the first 10 spaces.
Display: "You chose [school/career]."

# Ask the player to choose a career, depending on their path.
If "school":
    Input: Choose from college careers (professor, engineer, entrepreneur, doctor, etc.).
If "career":
    Input: Choose from non-college careers (artist, mechanic, influencer, etc.).
Set the salary based on the career.
Display: "Your chosen career is [career], with a salary of [$salary]."

#  Game Loop
# 2.1 Rolling the Die
# The player presses Enter to roll the die.
Input: Player presses Enter to roll.
Generate a random number (1 to 6) for the die roll.
Return the die roll as a number.

Move Player on the Board
# Update the player's position based on the die roll.
Add die roll to current position.
If position > 100, set position to 100 (end of the board).
Display: "You are now on space [position]."

# Call `board_events()` to handle events triggered when the player lands on a square.
Input: Player's position.
Call `board_events(player)`.

# Based on random die rolls, one of these events will occurs:
#  Unexpected Expense (subtract $100-$1000 from wealth).
# Buy a House (subtract house cost if affordable).
# Win a Prize (add $100-$1000 to wealth).
#  Family Milestone (vacation: subtract $500, or baby: subtract $50).
# Promotion (increase salary by 10%).

# every 8th square is a payday.
If position % 8 == 0 (payday):
    Add salary to wealth.
    Display: "It’s payday! You earned [$salary]. Your wealth is now [$wealth]."

end of game
# 3.1 The game ends when the player reaches space 100.
If position == 100:
    Calculate total wealth:
        Subtract education loan if applicable.
        Add 50% of the value of any owned properties.
    Display: "You have retired with a final wealth of [$total_wealth]. Congratulations!"

Mathematical operations and money/wealth adjustments
# Rolling the Die: random.randint(1, 6)' to simulate the die roll.
# Adjusting Wealth:
    # Unexpected Expense: wealth -= random.randint(100, 1000)
    # Prize Gain: wealth += random.randint(100, 1000)
    # House Purchase: If wealth >= house_cost, wealth -= house_cost and track property.
    # Vacation: wealth -= 500
    # Baby: wealth -= 50
    # Promotion: salary *= 1.10 (increase salary by 10%)
    # Property Value Calculation: property value at retirement = house_cost * 1.5

 Variables needed
# player (dictionary):
    # name: Player's name.
    # wealth: Player's current wealth (starting at $1000).
    # salary: Player's salary based on career choice.
    # position: Player's current position on the board (starts at 0).
    # properties: List of properties owned by the player.
    # loan: Education loan, if taken (starts at 0 or $40,000).

# board (list of 100 spaces):
    # Each space triggers a random event when landed on (e.g., unexpected expense, house purchase).
"""
