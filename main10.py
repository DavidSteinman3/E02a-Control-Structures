#!/usr/bin/env python3
import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!') # greets the player
colors = ['red','orange','yellow','green','blue','violet','purple'] # establishes all of those colors as possible answers
play_again = '' # allows the player the choice to play the game again
best_count = sys.maxsize            # the biggest number

while (play_again != 'n' and play_again != 'no'): # in the instance the player chooses not to play again by typing 'no' or 'n'
    match_color = random.choice(colors) # makes the right answer random out of the given color options
    count = 0 # number of tries is zero
    color = '' # players choose which color they think is correct
    while (color != match_color):
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip() # makes it so entries are not incorrect for capitalization or additional spaces
        count += 1 # counts the number of guesses the player uses
        if (color == match_color): # describes the instance the player guesses the right color
            print('Correct!') # the result if the player guesses right
        else: # describes the instance the player guesses incorrectly
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count)) # the result if the player is wrong
    
    print('\nYou guessed it in {} tries!'.format(count)) # tells the player how many guesses they used after the game

    if (count < best_count): # tells the player whether they guess in less tries than before
        print('This was your best guess so far!') # lets the player know this was the try they used the least amojunt of guesses
        best_count = count # allows program to remember this try as the best one so far

    play_again = input("\nWould you like to play again (yes or no)? ").lower().strip() # gives player the option of trying again

print('Thanks for playing!') # closing statement befoe game ends