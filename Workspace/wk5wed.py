import re


def isValidFile(string):
    return string.endswith(".py") or string.endswith(".pdf")

def isVal(string)
    regex = re.compile(r'[A-Za-z0-9] +\.(py\pdf)$')
    return re.search(regex, string)

print(isValidFile("q1.py"))
print(isValidFile("hwk.pdf"))
print(isValidFile("py.pdf"))
print(isValidFile("q1.cpp"))
print(isValidFile("hwk.pdf.txt"))
print(isValidFile("py.txt"))

email_regex = re.complie(r' [a-z]+\.([a-z.]+.)')