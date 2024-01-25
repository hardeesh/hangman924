import random

word_list = ["orange", "apple", "grapes", "pineapple", "mango"]

word = random.choice(word_list)

print(word)

def ask_for_input():
    while True:
        guess = input("Guess a letter: ")
        if len(guess) == 1 and str.isalpha(guess) == True:
            break
        else:
            print ("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)

def check_guess (guess):
    guess_lower = str.lower(guess)
    if guess_lower in word:
        print(f"Good guess! {guess_lower} is in the word.")
    else:
        print(f"Sorry, {guess_lower} is not in the word. Try again.")
    return (guess_lower)

ask_for_input()