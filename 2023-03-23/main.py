
"""
2 types of arguments:
- positional arguments: order matters
- keyword arguments: order does not matter

"""


# def get_name(name: str = 'John', age: int = 82):
#     return f'My name is {name} I am {age} years old.'
#
# print(get_name())


# def buy_item(item_code: str, count: int = 1, deliver_now: bool = True):
#     if deliver_now == True:
#         return f'You bought item {item_code} {count} times and will be delivered.'
#     else:
#         return f'You bought item {item_code} {count} times and will not be delivered.'
#
#
# print(buy_item('ABC345'))
# print(buy_item('X12'))
# print(buy_item('R042', deliver_now=False))


# def write_note(text: str, created: str, author: str = 'Mat', font: str = 'Arial'):
#     """
#     - text
#     - created date
#     - author
#     - font used
#     """
#     return f'{text} - {created} - {author} - {font}'
#
#
# message: str = write_note('Hello world', 'Mar 23, 2023', font='TNR', author='John')
# print(message)


# def attack(character: str, *, health: int, damage: int, ability: str, weapon: str, enemy: str = 'bots'):
#     return f'{character} attacks {enemy} using {weapon} with a damage of {damage} with the skill {ability} at health ' \
#            f'{health}.'
#
# message: str = attack('Ghost', health=100, damage=72, ability='Gain extra strength', weapon='assault rifle')
# print(message)
#
#
# """
# Enrolling new students
# - name
# - address
# - phone
# - mobile
# - highschool
# - year graduated
# - notes
# - birthday
# """

def student_enrollment(*, name: str, address: str, phone: str, mobile: str, highschool: str,
                       year_graduated: int, notes: str, birthday: str):
    return f'{name} - {address} - {phone} - {mobile} - {highschool} - {year_graduated} - {notes} - {birthday}'

message: str = student_enrollment(name='Dave', address='Makati', phone='123485', mobile='123456789',
                                  highschool='Ateneo', year_graduated=2022, notes='None',
                                  birthday='February 12')
print(message)
