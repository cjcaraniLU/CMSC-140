import re

#get users year of birth
year = int(input("Hello. What year were you born?: "))
#get info if user has had birthday
answer = input("Have you already had a birthday this year?: ")
age = -1
#while loop incase answer does not follow correct syntax. Will prompt user to re-enter their answer
yes_regex = re.compile(r"(y|Y|yes|Yes)") #not sure if this is the correct way to do this.
no_regex = re.compile(r"(n|N|no|No)")
while age == -1:
    # re.match()
    if(re.match(yes_regex, answer)):
         age = 2022 - year
    elif(re.match(no_regex, answer)):
        #add +1 to year because person has not had their birthday
        age = 2022 - (year +1)
    else:
        answer = input("Invalid answer. Try again: ")
print("You are ", age, " years old. ")