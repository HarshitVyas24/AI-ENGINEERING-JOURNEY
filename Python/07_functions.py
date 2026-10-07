def hello():
    print("Hello")

def sum(a,b = 2): #Parameters #default parameters 
    s = a+b
    return s

def avg(a,b,c):
    mean = (a+b+c)/3
    return mean

def factorial(n):
    if(n==1):
        return 1

    return n*factorial(n-1)

def factorial2(n):
    prod = 1
    for i in range(n,0 ,-1):
        prod*=i

    return prod


hello() #function call

print(sum(1)) #Arguments

print(avg(1,2,3))

print(factorial(5))
print(factorial2(5))