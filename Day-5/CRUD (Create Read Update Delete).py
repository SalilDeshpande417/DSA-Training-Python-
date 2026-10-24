import sys

class CRUD:
    def __init__(self):
        print("Student Management System")
        self.studentID=[]
        self.studentName=[]
        self.studentRollNo=[]
        self.studentCity=[]

    def addStudent(self):
        self.studentID.append(input("Enter student ID:"))
        self.studentRollNo.append(input("Enter student Roll No:"))
        self.studentName.append(input("Enter student Name:"))
        self.studentCity.append(input("Enter student City:"))

    def showStudent(self):
        print("Student details are:\n")
        print("StudentID\tStudentRollNo\tStudentName\tStudentCity")
        for x in range(65):
            print("-",end="")
        print()
        for i in range(len(self.studentID)):
            print(self.studentID[i],"\t\t",self.studentRollNo[i],"\t\t",self.studentName[i],"\t\t",self.studentCity[i])

            for x in range(65):print("-",end="")
            print()

    def updateStudent(self):
        newstudentID=input("Enter student ID: ")
        for i in range(len(self.studentID)):
            if newstudentID==self.studentID[i]:
                print("Matched Student Data Are: ")
                print("1 Student Roll No: ",self.studentRollNo[i],"\n2 Student Name: ",self.studentName[i],"\n3 Student City: ",self.studentCity[i],"\n4:Don't want to update:")
                ch=int(input("Select Above Option To Update: "))
                if ch==1:
                    self.studentRollNo.insert(i,input("Enter student Roll No: "))
                elif ch==2:
                    self.studentName.insert(i,input("Enter student Name: "))
                elif ch==3:
                    self.studentCity.insert(i,input("Enter student City: "))

    def deleteStudent(self):
        newstudentID=input("Enter student ID: ")
        k=0
        for i in self.studentID:
            if newstudentID==i:
                print("Matched Student Data Are: \n")
                print("1 Student Roll No: ",self.studentRollNo[k],"\n2 Student Name: ",self.studentName[k],"\n3 Student City: ",self.studentCity[k],"\n:Don't want to update:")
                ch=input("Do you really want to delete this record:(y/n) ")
                if ch=="y" or ch=="Y":
                    del self.studentID[k]
                    del self.studentRollNo[k]
                    del self.studentCity[k]
                    del self.studentName[k]
                else:
                    pass
            k=k+1

    def start(self):
        while True:
            print("\n1. Add Student")
            print("2. Show Student")
            print("3. Update Student")
            print("4. Delete Student")
            print("5. Exit")
            ch=int(input("Select any choice"))
            if ch==1:
                self.addStudent()
            elif ch==2:
                self.showStudent()
            elif ch==3:
                self.updateStudent()
            elif ch==4:
                self.deleteStudent()
            elif ch==5:
                sys.exit()
            else:
                print("please select correct choice..!\n")

if __name__ == '__main__':
    obj=CRUD()
    obj.start() 