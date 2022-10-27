def fsum(num1, num2):
    sum = 0
    for num in range(num1, num2+1):
        sum = sum + num
    return sum

#a = fsum(10,15)
#print(a)

def countdown(start, sub):
    print("Countdown start:")
    while start >= 0:
        print(start)
        start = start - sub

#countdown(18,4)

def function_chooser():
    print("Welcome to the function chooser. Please choose a function.")
    print("1 = Cumulative Sum")
    print("2 = Countdown")
    choice = int(input("Your choice: "))
    if(choice == 1):
        num1 = int(input("Enter a number ypu want the range to start at: "))
        num2 = int(input("Enter a number you want the range to end at: "))
        print ("The sum from ",num1, " to ", num2, " is ", fsum(num1, num2))
    elif(choice == 2):
        start = int(input("Enter a start number: "))
        sub = int(input("Enter a number to count down by: "))
        countdown(start, sub)
    else:
        print("Invalid option.")
            
function_chooser()