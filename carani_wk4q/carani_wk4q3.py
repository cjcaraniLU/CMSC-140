import random 
def random_number_guesser(guesses):
    guess_list = []
    number = random.randint(1,100)
    print("Welcome to the random number guesser. You have ", guesses, " guesses.")
    num_guess = guesses
    guess = int(input("Please input a number between 1 and 100: "))
    guess_list.append(guess)
    while guess != number and num_guess != 1:
        num_guess = num_guess - 1
        #compare the guess with the number the user is guessing
        if(guess > number):
            print(guess, " is too high. You have ", num_guess, " guess(es) left.")
            guess = int(input("Try again: "))
            guess_list.append(guess)
        else:
            print(guess, " is too low. You have ", num_guess, " guess(es) left.")
            guess = int(input("Try again: "))
            guess_list.append(guess)
    if(guess == number):
        print("Yes! ", guess, " is the correct number.")
    else:
        print("You are all out of guesses. ", guess, " is the correct number.")
    total = 0
    for num in guess_list:
        total = total + num
    return total/guesses

#asks user for how many guesses they will have for the game
guesses = int(input("How many guesses would you like to have?: "))
print("The avergae of all your guesses is: ", random_number_guesser(guesses))


#Q4 The average does not tell us much and depends on the actual number we are trying to guess. If the number we are trying to guess is large then the average will be larger since more guesses will be close in range to the actual number.