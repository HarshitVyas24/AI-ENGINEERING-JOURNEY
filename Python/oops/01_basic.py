class Student:
    subject = "Python"
    College = "ABC"
    year = "4th Year"

    def __init__(self, name, cgpa):
        print("Constructor was called...")
        self.name = name
        self.cgpa = cgpa

    def get_cgpa(self): #self is nothing but reference to the object for which this method will be called. SO, F
        return self.cgpa

stu1 = Student("Raghav", 9.2)
stu2 = Student("Rashmika", 9.8)
stu3 = Student("Manohar", 9)
print(stu1) #given memory address of this object in Main Memory
# print(stu1.subject , stu1.College , stu1.year)

print(stu1.name, stu1.cgpa)
print(stu1.name, stu1.cgpa)
print(stu3.name, stu3.cgpa)