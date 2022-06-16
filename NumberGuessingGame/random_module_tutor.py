# ----------Program to print random value from a list----------------
#import random module
import random;

#initialize your list - list_1
list_1 = [1, 2, 3, 4, 5]

# print a random value
print(random.choice(list_1))

# -------------------Program creates random number with a seeding value------------------------
random.seed(10)
print(random.random())
print(random.random())
print(random.random())
# Note: Random module create pseudo_random numbers/ Random numbers depend on the seeding value

# ------------------------------Creating random intergers-------------------
# Generates random number between two positive integers
# Note - Use of radint function
r1 = random.randint(5, 15)
print("Random number between 5 and 15 is % s" % (r1))

#Generates random number between two negative numbers
r2 = random.randint(-10, -1)
print("Random number between -10 and -1 is %s" % (r2))

