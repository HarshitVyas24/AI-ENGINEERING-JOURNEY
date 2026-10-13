def mostFreq(a) :
    maxi = 0
    for i in a:

        count = 0
        for j in range(len(a)):

            if a[j] == i:
                count += 1
        print(f"{i} , count = {count}")
        maxi = max(maxi , count)
    return maxi


def maxChar(s):

    return max(set(s) , key = s.count)

print(mostFreq("Apple"))
print(maxChar("Apple"))