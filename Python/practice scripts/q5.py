def chkPrime(a):

    isPrime = True

    i = 2
    while(i<a**0.5):
        if(a%i == 0):
            print(f"{a} is not a prime number!!")
            break
        else:
            print(f"{a} is a prime number!!")
            i+=1
                  
chkPrime(8)