class Payment:
    def pay(self):
        pass

class PayPalPayment(Payment):
    def pay(self, n):
        return f"paid {n} using paypal"

class CardPayment(Payment):
    def pay(self, n):
        return f"paid {n} using card"

p1 = PayPalPayment()
p2 = CardPayment()
print(p1.pay(100))
print(p2.pay(200))