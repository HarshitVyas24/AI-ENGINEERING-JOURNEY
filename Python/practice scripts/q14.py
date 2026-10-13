def ckhLeapYear(a):

    if(a%100 == 0):
        if(a%400 == 0):
            print("Leap year!!")
        else:
            print("Not a leap year")
    else:
        if(a%4 == 0):
            print("Leap year!!")
        else:
            print("Not a leap year")


ckhLeapYear(1800)