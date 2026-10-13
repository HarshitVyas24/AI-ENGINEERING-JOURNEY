def febonacci(n):

    first = 0
    sec = 1
    print(f"{first}, {sec}, " , end ="")
    for i in range(1,n):
        third = first + sec

        print(f"{third}, ", end="")

        first = sec
        sec = third

febonacci(10)

