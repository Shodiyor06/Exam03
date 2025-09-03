class Cart:
    def add_item(self, name, price):
        self.name = name
        self.price = price
    
    def get_totol_price(self):
        pass


cart = Cart()
cart.add_item("Laptop", 2000)
cart.add_item("Mouse", 100)
print(cart.get_total())