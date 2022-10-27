def alt_case(string):
    i = 0
    alt_string = ""
    print(len(string))
    for let in string:
        if(let == " "):
            alt_string = alt_string + " "
        elif(i % 2 == 0):
            alt_string = alt_string + let.upper()
            i = i + 1
        else:
            alt_string = alt_string + let.lower()
            i = i + 1
    return alt_string

my_string = "HeLLO World"
print(alt_case(my_string))