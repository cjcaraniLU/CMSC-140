def function(): 
    print("function")

def exponent(num1, num2):
    return num1 ** num2
ex1 = exponent(7,3)
ex2 = exponent(4, 2)
ex3 = exponent(25, .5)
#print(ex1)
#print(ex2)
#print(ex3)


def collatz(num):
    count = 0
    while(num != 1):
        if(num % 2 == 0):
            (num) = num/2
            (num) = int(num)
            count = count + 1
        else: 
            (num) = (num * 3) +1
            (num) = int(num)
            count += 1
    return("Length of chain: ", count)

#print(collatz(9))


def longest_collatz(start, end):
    longest_chain = 0
    for num in range(start, end):
        count = 0
        while(num != 1):
            if(num % 2 == 0):
                (num) = num/2
                count += 1
            else: 
                (num) = (num * 3) +1
                count += 1
        if(longest_chain < count):
            longest_chain = count
    return(longest_chain)

start = int(input("Enter num you want to start: "))
end = int(input("Enter the last number (included): ")) + 1
print("Longest chain: ", longest_collatz(start, end))