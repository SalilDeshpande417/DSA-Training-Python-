def power(base, exponent): #2 , 4
    if exponent == 0: #base condition 
        return 1
    return base * power(base, exponent-1)
print(power(2,0)) # 1
print(power(2,2)) # 4
print(power(2,4)) # 16 