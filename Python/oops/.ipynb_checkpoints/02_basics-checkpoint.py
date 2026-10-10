class Student:
    college_name = "ABC College" #class attribute
    pi  = 3.1
    def __init__(self, name, gpa):
        self.name = name #instance attributes
        self.gpa = gpa
        self.pi = 3.14

stu1 = Student("Rohan" , 10)

print(stu1.pi)
print(Student.pi)

#priority wise   -> instance att. > class att.