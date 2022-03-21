from art import logo, vs
from game_data import data
import random
import os

clear = lambda: os.system('cls')

def format_data(data):
	name = data['name']
	description = data['description']
	country = data['country']
	return f"Compare A: {name}, a {description}, from {country}."

score = 0
is_game_ended = False
first_random_person = random.choice(data)
while not is_game_ended:
	print(logo)
	if score > 0:
		print(f"You're right! Current score: {score}.")
	print(f"Compare A: {format_data(first_random_person)}")

	print(vs)

	second_random_person = random.choice(data)
	name = second_random_person['name']
	description = second_random_person['description']
	country = second_random_person['country']
	print(f"Against B: {format_data(second_random_person)}")

	answer = input("Who has more followers? Type 'A' or 'B': ")

	if (answer == "A" and first_random_person['follower_count'] > second_random_person['follower_count']) or (answer == "B" and first_random_person['follower_count'] < second_random_person['follower_count']):
		score += 1
		first_random_person = second_random_person
		clear()
	else:
		is_game_ended = True
		print(f"You lose. Your score {score}.")
