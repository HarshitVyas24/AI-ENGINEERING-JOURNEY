def chkArmstrong(a):
    cubeSum = 0
    for d in a:
        cubeSum += int(d)**3

    if(cubeSum == int(a)):
        print("Armstrong Number!!!!")

    else:
        print("Not an Artmstrong number!!!")

chkArmstrong("153")