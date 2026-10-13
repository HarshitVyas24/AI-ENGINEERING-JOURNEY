def isAnagram(a,b):

    a1 = sorted(a.lower())
    b1 = sorted(b.lower())

    if(a1 == b1):
        print('Anagram!!')
    else:
        print("Not Anagram!!")

isAnagram("listen" , "silent")