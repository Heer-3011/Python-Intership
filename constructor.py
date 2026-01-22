# class empolyee:
#     def __init__(self):
#         self.name=input("Enter Name of Employee:-")
#         self.field=input("Enter Field of Employee:-")
#         self.position=input("Enter position of Employee:-")
#         self.salary=int(input("Enter Salary of empolyee:-"))

#     def get_details(self):
#         print(f"Name= {self.name}\nField={self.field}\nPosition={self.position}\nSalary={self.salary}")


# emp1=empolyee() 
# print("Getting details.....")
# emp1.get_details()

#parametrized constructor
class student:
    def __init__(self,name,dep,enroll,cgpa):
        self.name=name
        self.dep=dep
        self.enroll=enroll
        self.cgpa=cgpa
    def show_details(self):
        print(f"Name={self.name}\nDepartment={self.dep}\nEnrollment={self.enroll}\nCGPA={self.cgpa}\n")

student1=student("Heer","IT",54009,9)
student1.show_details()