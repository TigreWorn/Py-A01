import random
word_list = ["python", "game", "computer", "laugh", "joke"]
word = random.choice(word_list)
guesses = []
turns = 10
while turns > 0:
    display_word = ""
    for letter in word:
        if letter in guesses:
            display_word += letter
        else:
            display_word += "-"
    print(display_word)
    guess = input("Guess a letter: ").lower()
    if guess in word:
        guesses.append(guess)
        print("Correct!")
    else:
        turns -= 1
        print("Wrong. You have", turns, "turns left.")
    if "-" not in display_word:
        print("Congratulations! You guessed the word.")
        break
if turns == 0:
    print("Game over. The word was", word)
