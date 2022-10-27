

#print("Here's a string for you! \nThis \\n is a newline command \nthat didn't actually do anything")

string = "C:\MyDocuments\Classes\Intro to Python\Week 5"
splitname = string.split()
print(splitname)

new_string = "-".join(splitname)
print(new_string)

space_string = "      Hello!  "
print(space_string.lstrip())
print(space_string.rstrip())
print(space_string.strip())