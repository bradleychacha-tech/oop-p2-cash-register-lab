
class CashRegister:
    def __init__(self, discount=0):
        self._discount = 0
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if type(value) == int and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, title, price, quantity=1):
        amount = price * quantity
        self.total += amount

        for _ in range(quantity):
            self.items.append(title)

        self.previous_transactions.append({
            "item": title,
            "price": price,
            "quantity": quantity,
            "amount": amount
        })

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
            return

        self.total = self.total * (100 - self.discount) / 100
        print(f"After the discount, the total comes to ${self.total:g}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        transaction = self.previous_transactions.pop()
        self.total -= transaction["amount"]

        for _ in range(transaction["quantity"]):
            self.items.remove(transaction["item"])

        if not self.items:
            self.total = 0.0
