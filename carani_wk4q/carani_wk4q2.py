classes = {
    "CMSC 140" : ["Intro to Python", "Ackles", 6, "M 9:50 - 11:00", "W 9:50 - 11:00", "R 10:25 - 12:10"],
    "I-E 100" : ["Innovation and Entrepreneurship", "Clayville", 6, "M 11:10 - 12:20", "W 11:10 - 12:20", "F 11:10 - 12:20"],
    "CMSC 510" : ["Data Structures and Algorithm Analysis", "Ackles, Gregg", 6, "M 3:10 - 4:20", "W 3:10 - 4:20", "F 3:10 - 4:20"]
}
for name in classes.keys():
    print("Course code: ", name)
    print("- Course Name: ", classes[name][0])
    print("- Professor: ",classes[name][1])
    print("- Units: ",classes[name][2])
    print("- Meets: \n   ", classes[name][3], "\n   ", classes[name][4], "\n   ", classes[name][5], "\n-----")

    