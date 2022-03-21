from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, direction):
	result = ""
	for letter in text:
		if letter in alphabet:
			index = alphabet.index(letter)
			if direction == "encode":
				index = index + shift
				if index > 25:
					result += alphabet[index - 25]
				else:
					result += alphabet[index]
			else:
				index = index - shift
				if index < 0:
					result += alphabet[25 + index]
				else:
					result += alphabet[index]
		else:
			result += letter
	if direction == "encode":
		print(f"Here's the encoded result: {result}")
	else:
		print(f"Here's the decoded result: {result}")


def start_fuction():
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))
	caesar(text, shift, direction)
	status = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
	if status == "yes":
		start_fuction()

print(logo)
start_fuction()

# 0 1 2 3 4 5 6 7 8 9 10111213141516171819202122232425
# a b c d e f g h i j k l m n o p q r s t u v w x y z
# h i j k l m n o p q r s t u v w x y z a b c d e f g 