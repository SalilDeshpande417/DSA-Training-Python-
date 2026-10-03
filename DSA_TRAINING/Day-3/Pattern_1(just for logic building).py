n = int(input("Enter the number of rows: "))
for i in range(1,n+1): #i = 1
    for j in range(1,n+1): # j = 2
        print(chr(64+i),end=" ") #ASCII
    print() 