# lambda a,b,c : expression like (a+b+c)
#lambda functions are used in place of higher order functions i.e, the function whixh either take some input parameters or retrun some value

sum = lambda a,b: a+b

calc_avg = lambda a,b,c : (a+b+c)/3

print(sum(4,5))
print(calc_avg(1,2,3))
