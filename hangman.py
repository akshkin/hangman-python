# Step 1
import random
import hangman_words
import hangman_art

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

word_length = len(chosen_word)
print(hangman_art.logo)

num_of_lives = 6
display = []

for blank in range(word_length):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You have already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"Your guess {guess} is not in the word. You lose a life.")
        num_of_lives -= 1
        if num_of_lives == 0:
            print("You lose")
    print(f"Lives remaining: {num_of_lives}")
    print(hangman_art.stages[num_of_lives])
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You guessed the word!!")
