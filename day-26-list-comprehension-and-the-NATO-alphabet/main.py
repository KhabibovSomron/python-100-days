#TODO 1. Create a dictionary in this format:
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

words = {row.letter: row.code for (index, row) in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    sentence = input("Input your name: ")

    try:
        result = [words[letter.upper()] for letter in sentence]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(result)

generate_phonetic()