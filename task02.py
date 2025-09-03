class Student:
    def __init__(self, name, age, level):
        self.name = name
        self.age = age
        self.level = level
    def introduce(self):
        return f"my name is {self.name}, i am {self.age} years old, studying in {self.level}nd course"
    
s = Student("ALI", 20, 3)
print(s.introduce())