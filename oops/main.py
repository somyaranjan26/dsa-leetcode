class Item:
    def __init__(self, name: str, price: float, qty=0):
        self.name = name
        self.price = price
        self.qty = qty
        
    def calculate_total_price(self):
        return self.price * self.qty
    
phone = Item("Phone", 100, 2)
laptop = Item("Laptop", 1000, 1)

# explictly setting the value of isTouchScreen
laptop.isTouchScreen = True
