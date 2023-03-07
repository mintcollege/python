from icecream import ic


class Student:
    idnum: int = None
    name: str = None
    course: str = None
    
    # Method
    def __init__(self, num: int, name: str, course: str):
        self.idnum = num
        self.name = name
        self.course = course
        
    def __str__(self):
        return self.name
    

sam = Student(6453445, 'Sam', 'CSIT')
print(sam)