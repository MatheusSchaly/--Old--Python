# Modify the program below to use a while loop to
# allow as many guesses as necessary.
#
# The program should let the player know whether to
# guess higher or lower, and should print a message
# when the guess is correct. A correct guess will
# terminate the program.
#
# As an optional extra, allow the player to quit by entering
# 0 (zero) for their guess.

import random

highest = 100
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())

while guess != answer:
    if guess == 0:
        break
    if guess < answer:
        guess = int(input("Please guess higher (or 0 to quit)\n"))
    else:
        guess = int(input("Please guess lower (or 0 to quit)\n"))
else:
    print("You have found the answer: " + str(answer))

if guess == 0:
    print("You quited")