class animal:
    def voice(self):
        self.v="Voice of animal"
        print(self.v)

class dog(animal):
    def dog_voice(self):
        self.v1="Brakkk"
        print(self.v1)

dog1=dog()
dog1.dog_voice()
dog1.voice()