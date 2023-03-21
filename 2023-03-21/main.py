from icecream import ic, IceCreamDebugger

class Npc:
    name: str
    age: int
    
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def give_gifts(self):
        return 'Gift has been given'
    
    def combat(self):
        return 'Fighting now'
    
    def eat(self):
        return 'Eating'
    
    def sleep(self):
        return 'zzzzzz'

class Male(Npc):
    gender: str
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.gender = 'male'

class Female(Npc):
    gender: str
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.gender = 'female'
        
    def combat(self):
        return 'I cannot fight'

alex = Male('Alex', 20)
haley = Female('Haley', 20)
print(alex.combat())
print(haley.combat())


class CustomIcecream(IceCreamDebugger):
    def __init__(self):
        super().__init__()
        self.enabled = False
        
cic = CustomIcecream()
cic('Hello')