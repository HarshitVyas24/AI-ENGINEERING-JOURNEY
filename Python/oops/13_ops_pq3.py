class Student:

    def __init__(self, name, roll_no, marks):
        self.__name =  name
        self.__roll_no = roll_no
        self.__marks = marks

    def set_info(self , name1 , roll , marks):

        self.__name = name1
        self.__roll_no = roll
        self.__marks = marks


    def get_info(self):

        # self.number = self.__marks
        # self.roll = self.__roll_no
        # self.name1 = self.__name1
        
        if(self.__name==""):
            print("Name cannot be empty string")
            exit()
        elif(self.__roll_no<1 or self.__roll_no>100 ):
            print("Invalid Roll_no!!")
            exit()
        elif(self.__marks<0 ):
            print("Marks cannot be Negative!")
            exit()
        else:    
            return {self.__name , self.__marks , self.__roll_no}


stu1 = Student("Harshit", 11, -90)
print(stu1.get_info())



        

