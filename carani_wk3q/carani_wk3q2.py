#import statement used to get a random number
import random 
#creates a function that plays a random word guesser game
def random_number_guesser(guesses):
    #generate a random number
    number = random.randint(1,100)
    print("Welcome to the random number guesser. You have ", guesses, " guesses.")
    #get the users guess
    num_guess = guesses
    guess = int(input("Please input a number between 1 and 100: "))
    #while loop that will continue to run until user guesses number or out of guesses
    while guess != number and num_guess != 1:
        num_guess = num_guess - 1
        #compare the guess with the number the user is guessing
        if(guess > number):
            print(guess, " is too high. You have ", num_guess, " guess(es) left.")
            guess = int(input("Try again: "))
        else:
            print(guess, " is too low. You have ", num_guess, " guess(es) left.")
            guess = int(input("Try again: "))
    if(guess == number):
        print("Yes! ", guess, " is the correct number.")
    else:
        print("You are all out of guesses.")

#asks user for how many guesses they will have for the game
guesses = int(input("How many guesses would you like to have?: "))
random_number_guesser(guesses)