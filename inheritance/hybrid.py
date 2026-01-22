class a:
    def display_a(self):
        print("Method of class A")

class b(a):
    def display_b(self):
        print("Method of class B")

class c(a):
    
    def display_c(self):
        print("Method of class C")

class d(b,c):
    def display_d(self):
        print("Method of class D")

obj_d=d()
obj_d.display_a()
obj_d.display_b()
obj_d.display_c()
obj_d.display_d()