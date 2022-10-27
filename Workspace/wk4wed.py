#Dictionaries

prof_offices = {
    "Ackles" : ["Steitz 131", "Briggs 414"] , "Krebs" : "Briggs 411", "Gregg" : "Briggs 413"
}
#print(prof_offices)
#print(prof_offices.values())

#for name in prof_offices.keys():
    #print(name)

#for name, office in prof_offices.items():
   # print(name + " is in " + office)

   #practice

practice_dict = { 5: 20, 2: "Hello", "Hello" : 5}
#for key, value in practice_dict.items():
    #print("Key is: ", key, " Value is ", value)
practice_dict["Added"] = 1
#print(practice_dict)
#print(5 in practice_dict)

fridge = {
    "eggs" : 12,
    "milk" : 1,
    "cheese" : 2,
    "bread" : 3,
    "pizza" : 0.5
}

shopping_needs = ["eggs", "fruit", "milk", "juice"]

for need in shopping_needs:
    if(need in fridge):
        print("You already have ",fridge[need], " ", need)
    else: 
        print(need, " is not in the fridge")
