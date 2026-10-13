def calc(a,b,op):

    match op:
        case "+" :
            print(f"a + b = {a+b}") 
        case "-" : print(f"a - b = {a-b}")
        case "-" : print(f"a * b = {a*b}")
        case "/" : print(f"a + b = {a/b}")
        case __:
            print("Invalid Operation")


calc(1,2,"+")