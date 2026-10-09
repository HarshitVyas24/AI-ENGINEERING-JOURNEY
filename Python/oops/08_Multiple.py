class Teacher:

    def __init__(self, subject, salary):
        self.subject = subject
        self.salary = salary


class Student:
    year = "2nd Year"

    def __init__(self, fee):
        self.fee = fee


class TA(Teacher, Student):

    def __init__(self, salary,subject, fee, name):
        super().__init__(subject ,salary)
        Student.__init__(self,fee)

        self.name = name


ta1 = TA(50_000 , "Reinforcement Learning" , 100000 , "Abhay")

print(F"year= {ta1.year} , salary= {ta1.salary}, subject= {ta1.subject}, fee= {ta1.fee}, name= {ta1.name}.")

