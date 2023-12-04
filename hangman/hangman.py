import random

def display_welcome():
    print("HANGMAN")
    print("The game will be available soon.")

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '-'
    print(display)

def play_hangman():
    words_list = ['python', 'java', 'javascript', 'php']

    while True:
        secret_word = random.choice(words_list)
        attempts_left = 8
        guessed_letters = []

        display_word(secret_word, guessed_letters)

        while attempts_left > 0:
            letter = input("Input a letter: > ")

            if not letter.isalpha() or not letter.islower() or len(letter) != 1:
                print("Please enter a lowercase English letter.")
                continue

            if letter in guessed_letters:
                print("You've already guessed this letter")
                continue

            guessed_letters.append(letter)

            if letter not in secret_word:
                print("That letter doesn't appear in the word")
            else:
                print("No improvements")

            display_word(secret_word, guessed_letters)

            if all(letter in guessed_letters for letter in secret_word):
                print(f"You guessed the word {secret_word}!")
                print("You survived!")
                break

            attempts_left -= 1

        if attempts_left == 0:
            print("You lost!")

        play_again = input("Type \"play\" to play again, \"exit\" to quit: ").lower()
        if play_again != "play":
            break

while True:
    print("Type \"play\" to play the game, \"exit\" to quit: ", end="")
    choice = input("> ")

    if choice.lower() == "play":
        display_welcome()
        play_hangman()
    elif choice.lower() == "exit":
        break
    else:
        print("Invalid choice. Please enter \"play\" or \"exit\".")
