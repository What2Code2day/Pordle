import os
from colorama import Fore, Back, Style
import random
os.system("")
print(f"\nWelcome to Pordle, the rules are the same as normal wordle, good luck")
# verifys the word you entered is a real word
valid_list = []
valid_file = open("valid-words.txt")
for word in valid_file:
    valid_list.append(word.strip())
# picks a random word from the words.txt file
word_list = []
word_file = open("words.txt")
for word in word_file:
    word_list.append(word.strip())
final_word = random.choice(word_list)

num_of_guess = 6


while num_of_guess > 0:
    guess = input(Fore.WHITE + f'\nGuess: ')
    letter_count = len(guess)
    if letter_count < 5 or letter_count > 5:
        print("The word you entered is too long or too short")
        continue
    elif guess not in valid_list:
        print(Fore.WHITE+'Not A Word')
        continue
    else:
        pass
    if letter_count < 5 or letter_count > 5:
        print("The word you entered is too long or too short")
        continue
    if guess == final_word:
        print('Correct! The word was', final_word)
    for i in range(5):
        if guess[i] == final_word[i]:
            print(Fore.GREEN, final_word[i].upper(), end=" ")
        elif guess[i] in final_word:
            print(Fore.YELLOW, guess[i].upper(), end=" ")
        else:
            print(Fore.WHITE, guess[i].upper(), end=" ")
    print(Fore.CYAN + f"\n-------------------------------------")
    num_of_guess -= 1
    if guess == final_word:
        print('Correct! You got it in', num_of_guess, 'guess!!')
    elif guess != final_word and num_of_guess == 0:
        print("Nice try, but the word was", final_word)
