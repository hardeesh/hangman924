import random

guess = input("Guess a letter: ")

if len(guess) == 1 and str.isalpha(guess) == True:
    print ("Good guess!")
else:
    print ("Oops! That is not a valid input.")

word_list = ["orange", "apple", "grapes", "pineapple", "mango"]

word = random.choice(word_list)

print(word)