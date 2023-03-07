import random
from icecream import ic

# class Voter:
#     name: str
#     address: str
#     age: int
#     candidate: str
#
#     def __init__(self, name: str, address: str, age: int):
#         self.name = name
#         self.address = address
#         self.age = age
#
#     def vote(self, votedfor: str):
#         self.candidate = votedfor
#
#
# sally = Voter('Sally Santos', '123 Temple Drive', 24)
# sally.vote('Von')
# print(f'Sally voted for: {sally.candidate}')


# class Car:
#     color: str
#
#     def __init__(self, color: str):
#         self.color = color
#
#     def run(self):
#         print('Running')
#
#     def stop(self):
#         print('Stopping')
#
#     def change_oil(self):
#         print('Changing oil')
#
#
# class Driver:
#     def buyfood(self):
#         pass
#
# mazda = Car('red')
# mazda.run()
# mazda.stop()
# mazda.change_oil()
#
#
# # class Weapon:
# #     level: int = 1
# #
# #     def upgrade(self):
# #         self.level += 1
#
# class Hero:
#     username: str
#
#     def __init__(self, name: str):
#         self.name = name
#
#     def attack(self):
#         damage: int = random.randint(0, 10)
#         print('Hero is attacking')
#         return damage
#
# class Dragon:
#     life: int = 100
#
#     def take_damage(self, damage: int):
#         self.life -= damage
#
#     def breathe_fire(self):
#         print('Dragon is breathing fire')
#
#     def eat(self):
#         pass
#
#
# nicole = Hero('Nicole')
# dragon = Dragon()
# damage: int = nicole.attack()
# dragon.take_damage(damage)
#
#
#
# class Student:
#     def partial_payment(self):
#         pass
#
#     def full_payment(self):
#         pass
#
#     def work_on_group_project(self):
#         pass
#
#     def signin(self):
#         pass
    
    
    

class Triangle:
    angles: list = []
    
    def add_angle(self):
        if len(self.angles) < 3:
            val = int(input('Type in an angle: '))
            self.angles.append(val)
        else:
            print('You have too many angles')
    
    def check_angles(self) -> str:
        total = sum(self.angles)
        if total == 180:
            return 'It is a valid triangle'
        return 'Not a valid triangle'
    
tri = Triangle()
tri.add_angle()
tri.add_angle()
tri.add_angle()
ic(tri.check_angles())