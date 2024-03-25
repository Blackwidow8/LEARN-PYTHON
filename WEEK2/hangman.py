import random

words = ["apple", "new", "hangman", "bear"]

word = random.choice(words)
print(word)
hidden = ["_"] * len(word)

guessed = []

failed_attempts = 0


# cannot insert two characters
# cannot attempt more than 6 times
# cannot select characters more than twice
# should only be letters

while "_" in hidden and failed_attempts < 6:
    print(''.join(hidden))
    print("Guessed letters", guessed)
    guessedChar = input("Guess a character:")

    if len(guessedChar) != 1:
        print("Enter a single character")
        continue
    if guessedChar in guessed:
        print("You already picked this character")
        continue
    if guessedChar.isalpha() == False:
        print("Enter a valid character")
        continue

    guessed.append(guessedChar)

    if guessedChar in word:
        for i in range(len(word)):
            if word[i] == guessedChar:
                hidden[i] = guessedChar
    else:
        failed_attempts += 1
        print(
            f"You entered a wrong character. Left with {6 - failed_attempts}")


if failed_attempts == 6:
    print("You lost")
else:
    print("You won")
    print(f"The word is {word}")