string = "hello"

for var in string : #in checks presence
    print(var)

if 'o' in string :
    print("Hi")


# word = "artificial intelligence"

# count = 0
# for i in word:
#     if i=="i":
#         count+=1
# print(count)

word = "artificial"

cnt = 0
for i in word:
    if i in ['a' ,'e' , 'i' , 'o' , 'u']:
        cnt += 1
print(cnt)


# range(start, stop, step)

for i in range(1,5,1):
    print(i)


sum= 0
for i in range(1,6,1):
    sum +=i

print(sum)