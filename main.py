import random
import os
import hangman_art
from hangman_words import word_list


chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo + "\n")

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("\nGuess a letter: \n").lower()
    os.system("clear")

    if guess in display:
        print(f"You already guessed '{guess}'!")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        print(f"\nI'm sorry, '{guess}' is not in the word!\n")
        if lives == 0:
            end_of_game = True
            print(f"You lose. The word is {chosen_word}")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])