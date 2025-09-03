class Temprature:
    def __init__(self, isiqlik):
        self.issiqlik = isiqlik
    @property
    def celsius(self):
        return self.issiqlik
    @property
    def fahrenheit(self):
        f = self.issiqlik * 9/5 + 32
        return f

t = Temprature(0)
print(t.celsius())
print(t.fahrenheit)
