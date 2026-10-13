def revNum(a):

    num = a
    revNum = 0

    while(num != 0):
        last_digit = num%10
        revNum= revNum*10 + last_digit
        num = num//10

    print(f"Reversed number is {revNum}")

revNum(1334)