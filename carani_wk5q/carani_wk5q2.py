major_courses = [
    "BIOL 130",
    "BIOL 150",
    "BIOL 280",
    "PHYS 141",
    "PHYS 151",
    "GEOL 110",
    "GEOS 210",
    "BIOL 650"
]

def filter_classes(list):
    class_codes = [] 
    for class_name in major_courses:
        if(class_name[0:4] == "BIOL"):
            class_codes.append(int(class_name[5:8]))
    return class_codes

codes = filter_classes(major_courses)
print(codes)