# Word Guessing Game in Python


import random

# Here the user is asked to enter the name first
name = input("What is your name? ")

print("Good Luck ! ", name)

words = ['random', 'computer', 'science', 'programming',
'python', 'mathematics', 'player', 'condition', 'reverse', 
'water', 'board', 'geeks']

#function will choose one random word from this list of words
word = random.choice(words)

print("Guess the characters")

guesses = ''

# Any number of turns can be used here
turns = 12

while turns > 0:

    # Counts the number of times a user fails
    failed = 0

    # All Characters from the input word taking one at a time
    for char in word:

        # comparing that character with the character in guesses
        if char in guesses:
            print(char)

        else:
            print("_")

            # for every failure 1 will be incremented in failure
            failed += 1

    if failed == 0:
        # User will win the game if failure is 0 and 'You Win' will be given as output
        print("You win")

        #This print the correct word
        print("The word is: ", word)
        break

    # If user has input the wrong alphabet then it will ask user to enter another alphabet
    guess = input("guess a character: ")

    #Every input character will be stored in guesses
    guesses += guess

    #Check input with the character in word
    if guess not in word:

        turns -= 1

        #if the character doesn't match the word then "wrong" will be given as output
        print("Wrong")

        #This will print the number of turns left for the user
        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You Loose")


            