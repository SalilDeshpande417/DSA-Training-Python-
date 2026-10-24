import csv 
f = open("student.csv","a",newline="")
a = csv.writer(f)
# a.writerow(["studentID","rollno","name","mobileno"]) # if you will not comment this it will write the column (["studentID","rollno","name","mobileno"]) every time

studentid = int(input("Enter student id: "))
rollno = int(input("Enter your rollno: "))
name = input("Enter your name")
mobileno = int(input("Enter your mobileno:"))
a.writerow([studentid,rollno,name,mobileno])
print("student record has save") 