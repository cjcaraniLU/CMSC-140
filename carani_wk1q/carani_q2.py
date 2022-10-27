print("Welcome to the random number guesser")
#answer is the number that the user is trying to guess
answer = 5
print("Please input a number between 1 and 10: ")
#guess is the users guess
guess = input()
# I then cast guess and answer to strings so that they will concatinate
print("You chose " + str(guess) + ". The number I chose was " + str(answer) + ". Did you guess it?")