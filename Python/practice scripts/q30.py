def isPangram(a):

    alpha = set("abcdefghijklmnopqrsstuvwxyz")

    if (alpha.issuperset(a)):
        print("Pangram")
    else:
        print("Not Pangram")

isPangram("zyx+")


