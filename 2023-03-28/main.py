from datetime import datetime

class Discord:
    # username: str
    # password: str
    
    def __init__(self, username: str, password: str, firstname: str, lastname: str):
        self.username = username
        self.password = password
        self._firstname = firstname
        self._lastname = lastname
        
    def enter_group(self, name: str):
        return f'You have entered the group {name}'
    
    @classmethod
    def stream(cls):
        return 'I am streaming'
    
    @staticmethod
    def get_date_today():
        return datetime.now()
    
    @property
    def fullname(self):
        return f'{self._firstname} {self._lastname}'
    
    @fullname.setter
    def fullname(self, newname: str):
        mylist = newname.split()
        self._firstname = mylist[0]
        self._lastname = mylist[1]
    
    
# nicole = Discord('bianca', 'passwordthatissecure', 'Bianca', 'Madrazo')
# print(nicole.fullname)
# nicole.fullname = 'Nicole Santos'
# print(nicole.fullname)


class Atm:
    pass


class User:
    pass


