#function that returns the number that creates the longest chain
def longest_collatz(start, end):
    #holds the value of the longest chain
    longest_chain = 0
    #holds the value of what number the loop is on
    tracker = 0
    #holds the value of the number that creates the longest chain
    num_prod = 0 
    for num in range(start, end):
        count = 0
        tracker = num
        #create collatz chain
        while(num != 1):
            if(num % 2 == 0):
                (num) = num/2
                count += 1
            else: 
                (num) = (num * 3) +1
                count += 1
        if(longest_chain < count):
            longest_chain = count
            num_prod = tracker
    return(num_prod)

start = int(input("Enter num you want to start: "))
end = int(input("Enter the last number (included): ")) + 1
print("Number that produced the longest chain: ", longest_collatz(start, end))