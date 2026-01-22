class grandparents:
    def display_grandparents(self):
        print("Method of grandparent")

class mother(grandparents):
    def display_mother_method(self):
        print("Method of Mummaaaa")

class child(mother):
    def display_child_method(self):
        print("Method of child")

c1=child()
c1.display_child_method()
c1.display_mother_method()
c1.display_grandparents()