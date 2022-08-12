# Import time module
import time


# Define the countdown function
def countdown(t):

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print("End")


# Take user input
t = input("Enter time in seconds: ")

# Function call
countdown(int(t))