class Employee:

    start_time =   "10 am"
    end_time = "6 pm"


class SchoolStaff(Employee):

    def __init__(self, role):
        self.role = role

class Faculty(SchoolStaff):
    def __init__(self, subject , role):
        super().__init__(role)
        self.subject = subject



t1 = Faculty("Computer Networks", "Assitantv Professor")

print(t1.subject,", ", t1.role , ", ", t1.start_time  , t1.end_time)