class empolyee:
    count=0
    def __init__(self):
        self.count+=1

    def set_details(self):
        self.name=input("Enter Name of Employee:-")
        self.field=input("Enter Field of Employee:-")
        self.position=input("Enter position of Employee:-")
        self.salary=int(input("Enter Salary of empolyee:-"))

    
class developer(empolyee): 
    def get_details(self):
        print(f"Name= {self.name}\nField={self.field}\nPosition={self.position}\nSalary={self.salary}")


d=developer()
d.set_details()
d.get_details()

print("count=",d.count)