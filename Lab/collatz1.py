#CJ Carani 09/22/22
#Get number from user that will go into while loop
num = (int)(input("Choose a postive number: ")) 
# keep track of length of chain
count = 0
#we want to stop when num gets to 1
while(num != 1):
    # if number is even divide y two
    if(num % 2 == 0):
        (num) = num/2
        # cast num to be an int instead of float
        (num) = int(num)
        # add one to counter/ length of chain
        count = count + 1
        print("Div by 2" + str(num))
    else: 
        #else multiply num by 3 and add 1 if num is odd
        (num) = (num * 3) +1
         # cast num to be an int instead of float
        (num) = int(num)
        # add one to counter/ length of chain
        count += 1
        print("Times by 3 plus 1: " + str(num))

print ("Final : " + str(num)) # should be one
print("Length of chain: " + str(count)) 