import random
import hangman_art as arts
import hangman_words as words

print(arts.logo)

chosen_word = random.choice(words.word_list)
word_length = len(chosen_word)
print(f"Chosen word:{chosen_word}")
display_word_list = []

for letter in chosen_word:
    display_word_list.append("_")

status = "start"
lives = 6
while status == "start":
    guess = input("Guess a letter: ").lower()

    for i in range(word_length):
        if guess == chosen_word[i]:
            display_word_list[i] = guess

    print(display_word_list)
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(arts.stages[lives])

    if "_" not in display_word_list:
        status = "win"
    elif lives == 0:
        status = "lose"

if status == "win":
    print("You win!")
else:
    print("You lose!")
