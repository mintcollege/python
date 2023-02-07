def get_data(age=12, name=None) -> int:
    return age

# print(get_data())


# def create_user(username: str, password: str, address=None, gender: str = None):
#     print(username, password, address, gender)
#
# create_user('von246', 'pass123', gender='m')

# age = 12
# def abc(age_: int, list_: list):
#     # global age
#     # age = 16
#     print(age)
#
# abc(age)


def getsum(*args):
    total = 0
    for i in args:
        total += i
    print(total)
#
# getsum(1, 4, 6, 2, 99)

def demo(abc: int, def_: int, *args, **kwargs) -> int:
    """
    This function is used to create valid users
    :param
    :param def_:        int
    :param args:        something
    :param kwargs:      something
    :return:            int
    """
    print(abc, def_, args, kwargs)
    return 123

demo(12, 45, 67, 345, 987, hello='world', age=12, price=24, score=12.5)