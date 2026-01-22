class student:
    name="Heer"
    sem="8"
    dep="Information Technology"
    def display(self):
        print(self.name,self.sem,self.dep)

s1=student()
s1.display()

class student1:
    def display(self,name,dep):
        print(name,dep)

s2=student1()
s2.display("Heer","IT")

class student2:
    def display(self,name,dep):
        return name,dep
s3=student2()
print(s3.display("Heer","IT"))

class student3:
    def display(self):
        return "Heer"

s4=student3()
print(s4.display())