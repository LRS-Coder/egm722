import random

# pick a random number for the user to guess
rand = random.randint(1, 20)

# adds a counter to keep track of number of guesses
count = 0

print('Guess a number between 1 and 20.')
guess = int(input())  # number needs to be an integer
count += 1

while guess != rand:  # if the guess is not equal to the random number, you have to guess again
    if guess > rand:  # if the guess is too high, tell the user.
        print('Too high. Guess again. Number of guesses is {}.'.format(count))
    else:  # if the guess is too low, tell the user.
        print('Too low. Guess again. Number of guesses is {}.'.format(count))

    print('Enter a new guess: ')
    guess = int(input())
    count += 1

print('You got it in {} guesses! The number was {}'.format(count, rand))
