def factorial(num): #num 1
    if num <= 1: # base condition
        return 1
    return num  *  factorial(num-1)
print(factorial(5)) 

# 5*factorial(4)
# 4*factorial(3)
# 3*factorial(2)
# 2*factorial(1)
#5*4*3*2*1 = 120
