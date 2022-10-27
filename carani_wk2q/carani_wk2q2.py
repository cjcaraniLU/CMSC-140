#ask user for number that you will subtract from
number = int(input("Please enter a number to start from: "))
#ask user for num that we will use to subtract
sub = int(input("Please enter how much you want to count down by: "))
print("Countdown: ")
#while loop that will execute until number is >= 0
while (number >= 0):
    print(number)
    number = number - sub