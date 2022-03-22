import random
from hangman_art import *
from hangman_words import *

print(logo)
word = random.choice(word_list)
display = []
for _ in word:
    display.append("_")
end_of_game = False
player_life = 6
print(f"Pssst, The solution is {word}")
# --------------------------
while not end_of_game:

    letter_chosen = input("Guess a letter: ").lower()
    if letter_chosen not in display:

        if letter_chosen in word:
            for x in range(len(word)):
                if letter_chosen == word[x]:
                    display[x] = letter_chosen

        if letter_chosen not in word:
            player_life -= 1
            print(f"You guessed {letter_chosen}, that's not in the word. You lose a life")

        if "_" not in display:
            print("You Won!")
            end_of_game = True

        if player_life <= 0:
            print("You Lost")
            end_of_game = True
    else:
        print(f"You've already guessed {letter_chosen}")

    print(f"{' '.join(display)}")
    print(stages[player_life])
