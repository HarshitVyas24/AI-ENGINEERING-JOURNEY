def chkPalindrome(a):
    num  = a
    revNum = 0
    while(num!=0):

        last_digit = num%10
        revNum = revNum*10 + last_digit
        num = num//10

    if(revNum == a):
        print("Palindrome!!")
    else:
        print("Not a Palindrome!!!!")

    
chkPalindrome(121)