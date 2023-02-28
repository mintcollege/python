import random as r
from icecream import ic
from computations import addnumbers as adder, generate_password


num1 = r.randint(1, 60)
num2 = r.randint(1, 60)

# total = adder(num1, num2)
# ic(total)

passlen = int(input('How long do you want your password to be? '))
passwd = generate_password(passlen)
ic(f'Password: {passwd}')