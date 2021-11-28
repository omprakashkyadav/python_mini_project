# Number Guessing Game
# Minimum NUmber of guessing = log2(upper_bound - lower_bound+1)

###################################
### Algorithms: Steps Below:   ####
###################################
# User Inputs the lower bound and upper bound
# The compiler generates a random integer between the range and store it in a variable for future references
# For repetitive guessing, a while loop will be initialized.
# If the user guessed a number which is greater than a randomly selected number, the user gets an output “Try Again! You guessed too high“
# Else If the user guessed a number which is smaller than a randomly selected number, the user gets an output “Try Again! You guessed too small”
# And if the user guessed in a minimum number of guesses, the user gets a “Congratulations! ” Output.
# Else if the user didn’t guess the integer in the minimum number of guesses, he/she will get “Better Luck Next Time!” output.
# Source - GeekforGeeks



import random
import math

#Take the Input for lower bound
lower_bound = int(input("Enter lower bound:- "))

# Take the Input for Upper bound
upper_bound = int(input("Enter Upper bound:- "))

#Generating the number b/w lower and upper bound
n = random.randint(lower_bound, upper_bound)
print("You have only", round(math.log(upper_bound - lower_bound + 1, 2)), "Chances to guess the integer!\n")

# Initializing the number of guesses.
count = 0

# for calculation of minimum number of guesses depends upon range
while count < math.log(upper_bound - lower_bound + 1, 2):
    count += 1

    # Taking guesssing nuber as input
    guess = int(input("Guess a numbber:- "))

    # Condition testing
    if n == guess:
        print("Congratulations you did it in", count, " try")
        # Once guessed, loop will break
        break

    elif n > guess:
        print("You guesse too small")
    elif n < guess:
        print("You Guessed too high!")

# If Guessing is more than required guesses
# Shows this output
if count >= math.log(upper_bound - lower_bound + 1, 2):
    print("\nThe number is %d" % n)
    print("\tBetter Luck next time!")


