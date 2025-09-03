class Person:
    def __init__(self, name, age, work):
        self.name = name
        self.age = age
        self.work = work
    
    def get_info(self):
        return f"{self.name} , {self.age} years old, work at {self.work}"
class Employe(Person):
    def __init__(self, name, age, work):
        super().__init__(name, age, work)
    
    def get_info(self):
        return super().get_info()
    
e = Employe("Hasan", 25, "google")
print(e.get_info())