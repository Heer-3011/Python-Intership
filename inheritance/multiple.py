class frontend:
    lang=['HTML','CSS','JavaScript']
    def display_front_lang(self):
        print(self.lang)
        
class backend:
    lang=['Python', 'Java', 'PHP']
    def display_back_lang(self):
        print(self.lang)

class full_stack(backend,frontend):
    lang1=backend.lang+frontend.lang
    def display_full_lang(self):
        print(self.lang1)
        #print("JavaScript (with HTML/CSS) back-end including Python, Java, C#, Node.js (JavaScript), PHP, Ruby, Go, ")


full1=full_stack()
full1.display_back_lang()
full1.display_front_lang()
full1.display_full_lang()