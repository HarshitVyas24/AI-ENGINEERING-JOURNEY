def countWords(a):
    count = 0

    words_lst = a.strip().split(" ")

    for i in words_lst:
        count += 1

    print(count)

countWords("Hello how are you")