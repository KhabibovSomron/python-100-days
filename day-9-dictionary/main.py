import os

clear = lambda: os.system('cls')

print("Wecome to the secret auction program.")

status = "start"
players = {}
while status == "start":
	name = input("What is your name?: ")
	bid = int(input("What's your bid?: $"))
	players[name] = bid

	other_player = input("Are there any other bidders? Type 'yes' or 'no'.\n")
	if other_player == 'no':
		status = "stop"
	else:
		clear()

winner_name = ""
winner_bid = 0
for key in players:
	if winner_bid < players[key]:
		winner_name = key
		winner_bid = players[key]

print(f"The winner is {winner_name} with a bid of ${winner_bid}.")
