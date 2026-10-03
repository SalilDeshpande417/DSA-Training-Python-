# WAP check two arrays are compatible or not
A = []
B = []
n1 = int(input('Enter the size of array :'))
for i in range(n1):
    A.append(input())
n2 = int(input('Enter the size of array :'))
for i in range(n2):
    B.append(input())
if len(A) == len(B):
    print('Compatible')
else:
    print('Not Compatible') 