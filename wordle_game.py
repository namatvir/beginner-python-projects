#May 1 2025

import nltk
import random

nltk.download('words')
from nltk.corpus import words

leng = int(input('How long would you like the word to be? '))

def get_word(leng: int):
    """returns a word randomly generated from nltk with length leng"""

    word_lst = words.words()
    words_select = []
    
    for word in word_lst:
        if len(word) == leng:
            words_select.append(word)
                     
    return  (random.choice(words_select))

wordle_word = get_word(leng).lower()

tries = int(input('How many tries would you like? '))

def guess_word():
    """
    returns feedback based on the guessed word inputted. ie:
    for letters that do not belong in word, user is told no 'X' in word.
    for letters that are misplaced in word, user is told 'X' is misplaced.
    for letters in the correct place, user is told 'X' is correct
    """

    i = 0

    while i < tries:

        guess = (input('What do you think the word is? ')).lower()

        if len(guess) > len(wordle_word):
            print('Word is too long.')

        elif len(guess) < len(wordle_word):
            print('Word is too short.')

        else:
            if guess == wordle_word:
                print('You guessed the word!')
                return ''
    
            else: 
                for letter in range(len(wordle_word)):

                    if guess[letter] == wordle_word[letter]:
                        print(guess[letter], ' is in the correct position.')
                    
                    elif guess[letter] in wordle_word:
                        print(guess[letter], ' is in the incorrect position.')
                    
                    else:
                        print(guess[letter], ' is not in the word')

            i += 1
    print('Out of tries, word is:', wordle_word)
    return ''

# print(wordle_word)
print(guess_word())

#for duplicate letters in either wordle word or guess specify if any are needed. 
#ie if dupes in guess but not word (where one letter is in word), specify first letter in word but second is not
#if dupes in word but not in guess, do nothing
#change so can only import real words aka words in nltk