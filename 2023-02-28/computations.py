from icecream import ic
import random


def addnumbers(val1: int, val2: int) -> int:
    """
    Adds 2 numbers
    :param val1: First number to add
    :param val2: Second number to add
    :return:    Total
    """
    ic(val1, val2)
    return val1 + val2

def generate_password(passlen: int) -> str:
    """
    Generates a random string which can be used for passwords.
    :param passlen: int Length of the string
    :return:        str
    """
    validchars = 'abcdefghijkmnpqrstuvwxyz0123456789'
    # ic(random.choice(validchars))
    
    final_password = ''
    for i in range(passlen):
        char = random.choice(validchars)
        final_password += char
        
    return final_password
    
# passwd = generate_password()
# ic(passwd)