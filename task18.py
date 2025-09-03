class Time:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __lt__(self, other):
        return (self.a + self.b) < (other.a + other.b)
t1 = Time(10, 30)
t2 = Time(12, 15)
print(t1 < t2)
