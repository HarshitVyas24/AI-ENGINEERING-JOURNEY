
#q1
# salary = int(input("Salary: "))

# if(salary<30000):
#     final = 0.5*salary
# elif(30000<=salary<=70000):
#     final = 0.15*salary
# else:
#     0.25*salary
# print("Final tax rate = ", final)

#q2

# def printEven(a,b):

#     for i in range(a,b+1):
#         if(i%2 ==0):
#             print(i)

# printEven(10,25)


#q3

def printDigits(n):

    new_num = n
    while(new_num != 0):
        digit = new_num%10
        print(digit)
        new_num = new_num//10


def countDigits(n):

    new_num = n
    count = 0
    while(new_num != 0):
        digit = new_num%10
        count +=1
        new_num = new_num//10
    print(count)


def sumDigits(n):

    new_num = n
    sum = 0
    while(new_num != 0):
        digit = new_num%10
        sum+= digit
        new_num = new_num//10
    print(sum)


def calculator(a,b,oprn):
    if oprn=="+":
        print("a+b = ", a+b)
    elif oprn=="-":
        print("a-b = ", a-b)
    elif oprn=="*":
        print("a*b = ", a*b)
    elif oprn=="/":
        print("a/b = ", a/b)


def isPrime(n):
    isPrime = True

    for i in range(2, n):
        if(n%i == 0):
            isPrime = False
    return isPrime

def guessTheNumber(my_guess ,  user_guess):

    if(user_guess > my_guess):
        print("Too High")

    elif(user_guess<my_guess):
        print("Too Low")

    else:
        print("Correct!")

# print(isPrime(129))

# calculator(1,2,"+")

my_choice= int(input("My choice: "))

user_guess = int(input("User Guess: "))

guessTheNumber(my_choice, user_guess )



# for i in range(1,100):
#     if (i%3==0 and i%5==0):
#         print(i)


# while(True):

#     num = input("num: ")

#     if(num == "Quit"):
#         break
#     elif(int(num)<0):
#         print("Negative")
#     elif(int(num)>0):
#         print("Positive")

#     else:
#         print("Ther number is 0")

# printDigits(312)
# countDigits(312232332)
# sumDigits(1234)

