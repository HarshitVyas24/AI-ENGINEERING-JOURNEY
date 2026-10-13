def cntDigit(n):

    num = n
    count = 0
    while(num!= 0):
        last_digit = num%10
        count+= 1

        num = num//10
    print(f"{count}")


cntDigit(1234)