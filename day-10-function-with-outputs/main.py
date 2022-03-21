from art import logo
import os

clear = lambda: os.system('cls')

def calculate(n1, n2, operation):
	if operation == "+":
		return n1 + n2
	elif operation == "-":
		return n1 - n2
	elif operation == "*":
		return n1 * n2
	elif operation == "/":
		return n1 / n2
	else:
		return "Invalid oepration"

def pick_oparation(n1):
	print("+\n-\n*\n/")
	operation = input("Pick an operation: ")
	second_number = float(input("What's the next number?: "))
	result = calculate(n1, second_number, operation)
	print(f"{n1} {operation} {second_number} = {result}")

	question = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
	if question == "y":
		pick_oparation(result)

while True:
	first_number = float(input("What's the first number?: "))
	pick_oparation(first_number)
	clear()



print(logo)