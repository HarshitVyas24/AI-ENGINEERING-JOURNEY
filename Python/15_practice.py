#ques1

# user_str = input("Enter a string: ").lower()

# if(user_str == user_str[::-1]):
#     print("Palindrome")
# else:
#     print("Not Palindrome")


#ques2


# int_list = [1,2,2,2,3]

# sum=0
# for val in int_list :
#     sum += val

# avg = lambda sum: sum/len(int_list)
# print(avg)

# #ques3

# list1 = []
# list2 = []

# for i in range (3):
#     num = int(input("Enter a element: "))
#     list1.append(num)
# for i in range (3):
#     num2 = int(input("Enter a element: "))
#     list2.append(num2)

# print(list1)
# print(list2)

# result = list1+list2
# print(result)

# result.sort()
# print(result)


#ques4

# t= (1,2,3,4,5,6,7,8,9,10)

# t_odd = tuple(val for val in t if val%2!=0)
# t_even = tuple(val for val in t if val%2 == 0)

# print(t_odd)
# print(t_even)


#ques5

# student_info = {}

# while True:
#     user_inpt = input("Enter operation : ")

#     if(user_inpt == 'A'):
#         name = input("name : ")
#         if name in list(student_info.keys()):
#             print("Student already Exists!")
#             print(student_info)
#         else:
#             student_info.update({name : None})
#             print("New Student Added!")
#             print(student_info)

#     elif(user_inpt == 'B'):
#         name = input("Name of student to update marks : ")
#         if name in list(student_info.keys()):
#             marks  = input("marks : ")
#             student_info[name] = marks
#             print("Marks updated")
#             print(student_info)
#         else:
#             print("Student do not exist!")

#     elif(user_inpt == 'C'):
#         name = input("Name: ")
#         if name in list(student_info.keys()):
#             print("Student Found")
#             print("Marks Secured : ", student_info.get(name))
#         else:
#             print("Student not found!!")

#     elif(user_inpt == 'D'):
#         print(student_info.items())

#     elif(user_inpt == 'Q'):
#         exit()

#     else:
#         print("Wrong User Input!")

#ques6

# words = ["apple" , "banana" , "kiwi", "cherry" , "mango"]

# fruits = {}

# for val in words :
#     if val in list(fruits.keys()):
#         print("Fruit Already exist")
#     else:
#         fruits.update({val : len(val)})
#         print("Updated!")

# print(fruits)


#ques7

# inpt_string= input("Enter a string: ")

# count = 0

# for char in inpt_string.strip():
#     if (char==" ") :
#         count+= 1
#     else:
#         continue

# print("The number of spaces = ",count)

#ques8

# list1 = [1,2,3,4,5]
# list2 = [4,5,6,7,8,9,10]

# if(set(list1).intersection(set(list2))==set()):
#     print("Given lists do not contain any common elements")
# else:
#     print("The given lists contains common elements")
#     print("common elements ",list(set(list1).intersection(set(list2))))

# #ques9

# list12 = [1,2,2,2,2,4,4,5]

# for val in set(list12) :
#     if(list12.count(val)>1):
#         print(val, " : ",list12.count(val), " times,\n")


#ques10

user_input= input("String: ")

unique_char = set()
for char in user_input.strip().lower() :
    
    unique_char.update(char)

unique_characters = list([x for x in unique_char])

print("The unique character are : ")
for x in unique_characters:
    print(x)

print("The number of unique characters in given string are: ", len(unique_char))









