a = [0, 1, 2, 3, 4, 5, 6, 7, 7, 9, 10, 11, 12, 13, 14, 16, 15, 17, 18, 18]
b = list(range(20))


def listdiff(a, b):  
    diff = [] #list that will hold values that are in b but not in a
    for i in range(20): 
        if(a[i] != b[i]): #iterate through both lists and compare each lists values
            diff.append(b[i])
    return diff

diff = listdiff(a, b)
print(diff)