#get users year of birth
year = int(input("Hello. What year were you born?: "))
#get info if user has had birthday
answer = input("Have you already had a birthday this year?: ")
age = -1
#while loop incase answer does not follow correct syntax. Will prompt user to re-enter their answer
while age == -1:
    if(answer == "Y" or answer == "Yes" or answer == "y" or answer == "yes"):
         age = 2022 - year
    elif(answer == "N" or answer == "No" or answer == "n" or answer == "no"):
        #add +1 to year because person has not had their birthday
        age = 2022 - (year +1)
    else:
        answer = input("Invalid answer. Try again: ")
print("You are ", age, " years old. ")