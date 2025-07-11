import random

secret_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100. Can you guess it?")

guesses = 0 

while True:
    try:
        user_guess = int(input("Enter your guess: "))
        guesses += 1
        if user_guess > secret_number:
            print("Too high! Try a lower number!")

        elif user_guess < secret_number:
            print("Too low! Try a higher number!")
        else:
            print("Congratulations! You guessed it right!") 
            print(f"It took you {guesses} guesses to find the number {secret_number}.")
            break

    except ValueError:
        print("Invalid input. Please enter a number between 1 and 100.")
        