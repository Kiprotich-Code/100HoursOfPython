# interactive guessing script
# Ask user to guess a number between 1 and 99
# !Important - lessons
# Random module and radint function
# While loop / conditional statements

import random
n = random.randint(1, 99)
guess = int(input("Enter an integer between 1 and 99: "))

while n != "guess":
    print
    if guess < n:
        print ("Guess is low")
        guess = int(input("Enter an integer between 1 and 99: "))
    elif guess > n:
        print ("Guess is high")
        guess = int(input("Enter an interger between 1 and 99: "))
    else:
        print("You guessed it!")
        break
    print