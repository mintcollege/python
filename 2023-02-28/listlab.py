from icecream import ic
from computations import generate_password


# fruits = ['apple', 'banana', 'coconut']
# fruits2 = [*fruits]
# sports = ['acrobatics', 'basketball', 'cheerleading']
# combined = [*fruits, *sports]
# ic(combined)
# ic(fruits2)
# fruits.append('dragon fruit')
# ic(fruits2)
# for i in fruits:
#     print(i)
# ic(fruits)

# user = {
#     'username': 'helloman123',
#     'password': generate_password(12)
# }
# user2 = {**user}
# ic(user)
# ic(user2)

# age = 12
# num = age
# ic(num)
# age = 24
# ic(num)
# age2 = 12
# ic(id(age))
# ic(id(num))


def get_fruits(datalist: list = None) -> list:
    if datalist is None:
        datalist = ['apple', 'banana', 'coconut']
    
    return datalist

myfruits = get_fruits()


# pluralized = []
# for i in myfruits:
#     plural = i + 's'
#     pluralized.append(plural)

# List comprehension
pluralized = [i + 's' for i in myfruits if i == 'coconut']

# {k: v for k, v in mydict.items()}

ic(pluralized)


