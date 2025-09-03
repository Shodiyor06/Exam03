class Animal:
    def __init__(self, name):
        self.name = name
    
    def bak(self):
        pass

class Dog(Animal):
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print("wow! wow!")

d = Dog("rex")
print(d.name)
d.bark()