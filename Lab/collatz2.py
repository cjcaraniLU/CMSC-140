#CJ Carani 09/22/22
# this variable keeps track of what the longest chain is
longest_chain = 0
# this variable keeps track of what number produces the longest chain
largest_num = 0
print("Enter the starting number(larger than 1): ")
start = int(input())
tracker = start -1
print("Enter the last number (included): ")
last = int(input()) + 1
for num in range(start, last):
    count = 0
    while(num != 1):
        if(num % 2 == 0):
            (num) = num/2
            count += 1
        else: 
            (num) = (num * 3) +1
            count += 1
    tracker += 1
    if(longest_chain < count):
        largest_num = tracker
        longest_chain = count
print("Longest Chain is from", largest_num)
print("Length of Chain: ", longest_chain)
# when range is 2 to 1000: Length of chain: 178 and Longest chain is from 871 
