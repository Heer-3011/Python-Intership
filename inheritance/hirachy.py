class a:
    def display_a(self):
        print("Method of class A")

class b(a):
    def display_b(self):
        print("Method of class B")

class c(a):
    
    def display_c(self):
        print("Method of class C")

class d(b):
    def display_d(self):
        print("Method of class D")

class e(c):
    def display_e(self):
        print("Method of class E")

class f(b):
    def display_f(self):
        print("Method of class F")
class g(c):
    def display_f(self):
        print("Method of class G")


obj_d=d()
obj_d.display_a()
obj_d.display_b() 
obj_d.display_d()

obj_e=e()
obj_e.display_a()
obj_e.display_c()
obj_e.display_e()

obj_f=f()
obj_f.display_a()
obj_f.display_b()
obj_f.display_f()