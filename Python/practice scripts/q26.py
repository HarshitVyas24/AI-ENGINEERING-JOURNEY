def removeDup(a):
    unique = set()
    for i in a:
        unique.add(i)

    new = ""
    for i in unique:
        new += i

    print(new)


removeDup("Apple")