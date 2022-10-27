import matplotlib.pyplot as plt
# 'a' appends to the file 'r' reads the file 'w' overwrites everything in the file 'r+' to both read and write
hello = open("hello.txt", 'w')
#print(hello)

#file_contents = hello.read()
#file_contents_list = hello.readlines() #gives us a list seperates by line
#print(file_contents)

#hello .write("\n Heres some new content")
hello.close()

with open("goodbye.txt") as f:
    info = f.readlines()
#print(info)

for i, val in enumerate(info):
    info[i] = val.strip()

names = open("names.txt", 'r+')

n = names.read()
#print(n)
#names.write("\nCJ Carani")
names.close()

temps = []
hats = []
with open("hats.txt") as f:
    next(f) #skips first line
    for line in f.readlines():
        line = line.strip()
        x, y = line.split(" ")
        temps.append(int(x))
        hats.append(int(y))
print(temps)
print(hats)

plt.plot(temps, hats)
plt.show()