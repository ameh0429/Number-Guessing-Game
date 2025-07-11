# Number Guessing Game

## Project Overview
This is a simple console-based number guessing game implemented in Python. The computer "thinks" of a random number within a specified range (1 to 100), and the player's goal is to guess that number. The game provides hints ("Too high!" or "Too low!") after each guess, helping the player narrow down the possibilities. The game tracks and displays the number of attempts it took to guess the correct number.

## Features
- Random Number Generation: The computer selects a random integer between 1 and 100 (inclusive) as the secret number.
- Interactive Guessing: Players can repeatedly enter their guesses.
- Hints System: Provides feedback to the player after each guess, indicating whether their guess was too high or too low.
- Guess Counter: Keeps track of the number of attempts the player makes.
- Win Condition: The game ends once the player correctly guesses the secret number.
- Summary: Displays the total number of guesses taken and the secret number upon winning.
- Input Validation: Handles non-numeric input gracefully, prompting the user to enter a valid number.

## How to Play
### Prerequisites
- Python 3.x installed on your system.

### Running the Game
- **Save the code**: Save the provided Python code into a file named `guessing_game.py` (or any other `.py` extension).
- **Open a terminal/command prompt**: Navigate to the directory where you saved `guessing_game.py`.
- **Run the script**: Execute the command:

```
python guessing_game.py
```

### Game Instructions
- Upon starting, the game will welcome you and inform you that it has chosen a number between 1 and 100.
- You will be prompted to Enter your guess: .
- Type a whole number between 1 and 100 and press Enter.
- **Hints**:
 - If your guess is too high, the game will say: "Too high! Try a lower number!"
 - If your guess is too low, the game will say: "Too low! Try a higher number!"
- **Winning**:
 - If your guess is correct, the game will congratulate you and tell you how many guesses it took to find the number.
 - The game will then end.
- **Invalid Input**: If you enter anything that is not a whole number (e.g., text, decimals), the game will prompt you to enter a valid number and will not count that as a guess.

## Code Structure
The game's logic is contained within a single Python script (`guessing_game.py`) and follows this structure:
- `import random`: Imports the `random` module, which is essential for generating the `secret_number`.
- `secret_number = random.randint(1, 100)`: This line generates the random target number for the game. For testing purposes during development, you might temporarily print(`secret_number`) but it should be removed or commented out for actual gameplay.
- `guesses = 0`: An integer variable initialized to zero, used to count the player's attempts.
- `while True:` **loop**: This is the main game loop. It continues indefinitely until the player guesses correctly and a break statement is executed.
- `try-except ValueError` **block**: Encapsulates the user input process.
 - `try:` Attempts to get user input (`input()`) and convert it to an integer (`int()`).
 - `except ValueError`: Catches errors if the user enters non-numeric text, printing an error message and allowing the loop to continue without crashing.
- `guesses += 1`: Increments the guesses counter with each valid attempt.
- `if/elif/else` **statements**: These conditional statements form the core game logic:
 - `if user_guess > secret_number`: Provides the "Too high!" hint.
 - `elif user_guess < secret_number`: Provides the "Too low!" hint.
 - `else`: This block is executed when `user_guess == secret_number`. It congratulates the player, prints the total `guesses`, and then uses `break `to exit the `while `loop, ending the game.

##  Key Concepts Demonstrated
This project effectively demonstrates and reinforces the following Python programming concepts:
- **Modules**: Importing and using the `random `module.
- **Variables**: Storing the `secret_number`, `user_guess`, and `guesses `count.
- **Input/Output**: Using `input()` to get user guesses and `print()` to provide game feedback.
- **Logic & Control Flow**:
 - while Loop`: `For repetitive guessing until a condition is met.
 - `if/elif/else` **Statements**: For decision-making based on guess comparison.
 - `break `**Keyword**: For exiting the game loop early upon a win.
- **Type Conversion**: Using `int()` to convert string input to an integer.
- **Counters**: Incrementing a variable to track progress.
- **Error Handling**: Basic `try-except` for `ValueError` to handle invalid input.
