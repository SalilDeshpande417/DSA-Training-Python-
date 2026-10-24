import csv 
f = open("student_1.csv","a",newline="")
a = csv.writer(f)
#a.writerow(["rollno","name","mobileno","p1","p2","p3","total","percentage","email","result"]) # if you will not comment this it will write the column (["studentID","rollno","name","mobileno"]) every time

rollno = int(input("Enter your roll no: "))
name = input("Enter your name")
mobileno = int(input("Enter your mobileno:"))
p1 = int(input("Enter P1: "))
p2 = int(input("Enter P2: "))
p3 = int(input("Enter P3: "))
email = input("Enter your email:")
total = p1+p2+p3
print(total)
percentage = total/3.0 
print(percentage) 
if p1>=40 and p2>=40 and p3>=40:
    result = "pass"
    print("You are Pass")
else:
    result = "fail" 
a.writerow([rollno,name,mobileno,p1,p2,p3,total,percentage,email,result])
print("student record has save") 