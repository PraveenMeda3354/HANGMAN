from hangman import stages , logo , word_list , fruits,vegetables,animals,birds,win
import random

hint = [
    "This is a fruit",
    "This is a vegetable",
    "This is an animal",
    "This is a bird"
]
print(logo)
print()

print("If you can't find the word.I will be")
print(stages[0])
print("Please help me!")
word = random.choice(word_list)
if word in fruits:
    print("Hint : ",hint[0])
elif word in vegetables:
    print("Hint : ",hint[1])
elif word in animals:
    print("Hint : ",hint[2])
else:
    print("Hint : ",hint[3])


word_length = len(word)

end_of_game = False
lives = 6

display = []
for _ in range(word_length):
    display += "_"

print(f"{' '.join(display)}")
used = []

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = word[position]

        if letter == guess:
            display[position] = letter

    if guess not in word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The given word is {word}")

    print(f"{' '.join(display)}")
    print(stages[lives])


    if "_" not in display:
        end_of_game = True
        print("You win.")
        print(win)



