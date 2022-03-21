with open("Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()

with open("Input/Letters/starting_letter.txt") as example_letter:
    letter = example_letter.read()

PLACEHOLDER = "[name]"

for name in names:
    stripped_name = name.strip()
    with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as file:
        new_letter = letter.replace(PLACEHOLDER, stripped_name)
        file.write(new_letter)

