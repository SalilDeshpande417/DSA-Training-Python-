import sys

class CRUD:
    def __init__(self):
        print("Student Management System")

        self.studentID = []
        self.studentName = []
        self.studentRollNo = []
        self.studentCity = []


    def addStudent(self):
        self.studentID.append(input("Enter student ID: "))
        self.studentRollNo.append(input("Enter student Roll No: "))
        self.studentName.append(input("Enter student Name: "))
        self.studentCity.append(input("Enter student City: "))

        print("Student added successfully!")

    
    def showStudent(self):
        print("\nStudent details are:\n")

        print("StudentID\tStudentRollNo\tStudentName\tStudentCity")

        for x in range(60):
            print("-", end="")
        print()

        for i in range(len(self.studentID)):
            print(
                self.studentID[i], "\t\t",
                self.studentRollNo[i], "\t\t",
                self.studentName[i], "\t\t",
                self.studentCity[i]
            )

        for x in range(60):
            print("-", end="")
        print()

    
    def updateStudent(self):
        student_id = input("Enter Student ID to update: ")

        if student_id in self.studentID:

            index = self.studentID.index(student_id)

            print("\nEnter new details:")

            self.studentRollNo[index] = input("Enter new Roll No: ")
            self.studentName[index] = input("Enter new Name: ")
            self.studentCity[index] = input("Enter new City: ")

            print("Student updated successfully!")

        else:
            print("Student ID not found!")

    
    def deleteStudent(self):
        student_id = input("Enter Student ID to delete: ")

        if student_id in self.studentID:

            index = self.studentID.index(student_id)

            # Delete student from all lists
            self.studentID.pop(index)
            self.studentRollNo.pop(index)
            self.studentName.pop(index)
            self.studentCity.pop(index)

            print("Student deleted successfully!")

        else:
            print("Student ID not found!")

    
    def start(self):
        while True:
            print("\n1. Add Student")
            print("2. Show Student")
            print("3. Update Student")
            print("4. Delete Student")
            print("5. Exit")

            ch = int(input("Select any choice: "))

            if ch == 1:
                self.addStudent()

            elif ch == 2:
                self.showStudent()

            elif ch == 3:
                self.updateStudent()

            elif ch == 4:
                self.deleteStudent()

            elif ch == 5:
                print("Thank you!")
                sys.exit()

            else:
                print("Please select correct choice..!\n")


if __name__ == '__main__':
    obj = CRUD()
    obj.start() 