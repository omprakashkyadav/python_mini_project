#Hangman Game

import random
from collections import Counter

somewords = '''apple banana mango straweberry orange grape pineapple apricot lemon
 coconut watermelon cherry papaya berry peach lychee muskmelon'''
print("1-", somewords)

somewords = somewords.split(' ')
print("2-", somewords)

# Randomely choose a secret word from our "somewords" LIST.
word = random.choice(somewords)
print("3-", word)

if __name__ == '__main__':
    print('Guess the word! HINT: word is a name of a fruit')

    for i in word:
        print(i)
        # For printing theempty spaces for letters of the word
        print('_', end=' ')
    print()

    playing = True
    # List for storing the letters guessed by the player
    letterGuessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0
    try:
        # Flag is updated when the word is correctly guessed
        while (chances != 0) and flag == 0:
            print()
            chances -= 1
            print("5-", chances)

            try:
                guess = str(input('Enter a letter to guess: '))
            except:
                print('Enter only a letter!')
                continue

            # Validation of the guess
            if not guess.isalpha():
                print('Enter only a LETTER')
                continue
            elif len(guess) > 1:
                print('Enter only a SINGLE letter')
                continue
            elif guess in letterGuessed:
                print('You have already guessed that letter')
                continue

            # if letter is guessed correctly
            if guess in word:
                # k stores the number of times the guessed letter occurs in the word
                k = word.count(guess)
                for _ in range(k):
                    # The guess letter is added as many times as it occurs
                    letterGuessed += guess

            # print the word
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                    print(char, end=' ')
                    correct += 1

                #If user has guessed all the letters
                elif (Counter(letterGuessed) == Counter(word)):
                    #Once the correct word is guessed fully, the game ends, even if chances remain
                    print("The word is: ", end=' ')
                    print(word)
                    flag = 1
                    print('Congratulations, You won!')
                    break # To break out of the for loop
                    break # To break out of the while loop
                else:
                    print('_', end=' ')

        if chances <= 0 and (Counter(letterGuessed)) != Counter(word):
            print()
            print('You lost! Try again..')
            print('The word was {}'.format(word))


    except KeyboardInterrupt:
        print()
        print('Bye! Try again, ')
        exit()



