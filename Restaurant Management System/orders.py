class Order:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):

        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self, item):

        if item in self.items:
            del self.items[item]

    @property
    def total_price(self):

        total = 0

        for item, quantity in self.items.items():
            total += item.price * quantity

        return total

    def clear(self):
        self.items = {}