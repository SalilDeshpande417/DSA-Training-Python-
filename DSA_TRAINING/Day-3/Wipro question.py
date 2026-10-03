n = int(input("Enter the value of N :"))
mylist = list(map(int, input().split())) 
sum = 0
for i in range(n-1):
   sum += abs(mylist[i] - mylist[i+1])
print("Sum = ",sum) 