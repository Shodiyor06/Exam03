class Flyer:
    def __init__(self, name):
        self.name = name
    def swim(self):
        print(f"{self.name} is flaying")
class Swimmer:
    def __init__(self, name):
        self.name = name
    def fly(self):
        print(f"{self.name} is swimming")

class Duck(Flyer, Swimmer):
    def __init__(self):
        self.name = 'duck'
    def swim(self):
        return super().swim()
    def fly(self):
        return super().fly()
duck = Duck()
duck.fly()
duck.swim()