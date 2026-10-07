info = [
    ("Alice" , "Math"),
    ("Bob" , "Science"),
    ("Alice" , "Science"),
    ("Charlie" , "Math"),
    ("Bob" , "Math"),
    ("Alice" , "English"),
    ("Charlie" , "English")
]

# New way of printing Elements together of a list

for name,course in info:
    print(name , ", ", course)

unique_courses = set()
for val in info:
    unique_courses.add(val[1])

print(unique_courses)


for val in info:

    if(val[1] == "English"):
        print(val[0])

dict= {}

for name, course in info:

    if(dict.get(name) == None):
        dict.update({name : set()})
        dict[name].add(course)
    else:
        dict[name].add(course)

print(dict)



