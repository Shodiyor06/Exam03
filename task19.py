import json
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def to_json(self):
        data = {"name": self.name, "price": self.price}
        with open("task19.json", "w") as f:
            json.dump(data, f, indent=4)

p = Product("Laptop", 1500)
print(p.to_json())