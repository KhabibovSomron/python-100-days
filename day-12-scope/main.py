import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm think of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
	attempts = 10
else:
	attempts = 5

is_guess = False

number = random.randint(1, 100)
print(number)
while attempts > 0 and not is_guess:
	print(f"You have {attempts} attempts remaining to guess the number.")
	guess_number = int(input("Make a guess: "))

	if guess_number > number:
		print("Too high.")
		attempts -= 1
		if attempts != 0:
			print("Guess again.")
	elif guess_number < number:
		print("Too low.")
		attempts -= 1
		if attempts != 0:
			print("Guess again.")
	else:
		print(f"You got it! The answer was {number}.")
		is_guess = True

	if attempts == 0:
		print("You've run out of guesses, you lose.")