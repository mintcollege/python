
class Waiter:
    def give_menu(self) -> list:
        return ['shrimp', 'hotdog', 'burger', 'sushi']
    
    def recieve_order(self, orders: list):
        pass


class Customer:
    menu: list
    orders: list
    
    def __init__(self, menu: list):
        self.menu = menu
    
    def make_order(self, code: str, *, count: int = 1):
        self.orders.append({
            'order': code,
            'count': count
        })
        
    def give_order(self) -> list:
        return self.orders
    
    def complain(self, message: str, anger_rating: int = 7):
        pass
    
    def ask_order_status(self, code: str, table: int):
        pass
    
    def pay(self, amount: float):
        pass


class Chef:
    def take_order(self, code: str, count: int, table: int):
        pass
    
    def cook_order(self, code: str, count: int):
        pass
    
    def give_status(self, code: str, table: int) -> str:
        return 'Still cooking'
    
    def give_food(self, food: str, table: int):
        pass

von = Waiter()
nic = Customer(von.give_menu())
nic.make_order('M3', count=3)
nic.make_order('F2', count=10)
von.recieve_order(nic.orders)


