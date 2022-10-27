#import statement used to get a random number
import random 
#generate a random number
number = random.randint(1,100)
print("Welcome to the random number guesser.")
#get the users guess
guess = int(input("Please input a number between 1 and 100: "))
#while loop that will continue to run until user guesses number. prompts user if they guess incorrectly
while guess != number:
    if(guess > number):
        print(guess, " is too high.")
        guess = int(input("Try again: "))
    else:
        print(guess, " is too low.")
        guess = int(input("Try again: "))
print("Yes! ", guess, " is the correct number.")