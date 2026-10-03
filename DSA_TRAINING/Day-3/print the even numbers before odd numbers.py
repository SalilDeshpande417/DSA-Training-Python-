N = 8
mylist = []
for i in range(N):
    val = int(input('Enter the value:'))
    mylist.append(val)
print(mylist)
A = []
B = []
for i in range(len(mylist)):
    if mylist[i]%2==0:
        A.append(mylist[i])
    else:
        B.append(mylist[i])
print(A)
print(B)
