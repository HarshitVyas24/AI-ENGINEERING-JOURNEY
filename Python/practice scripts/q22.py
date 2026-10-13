def chkStrPalindrome(a):

    if(a[::-1] == a):
        print("Palindrome")
    else:
        print("Not Palindrome")

chkStrPalindrome("mom")