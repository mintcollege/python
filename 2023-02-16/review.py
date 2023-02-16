from icecream import ic


# str interpolation
name = 'Dave'
age = 23
message = 'Hello {}. He is {} years old. {} {}'.format(name, age, name, name)
# message =
# print(f'Hello {name}. He is {age} years old. {name} {name} {age}')

# num = [2, 4, 6, 8]
# first, second, third, fourth = num
# print(first)
# print(second)
# for i in num:
#     print(i)

# key-val store
# userdata = {
#     # key    val
#     'name': 'dave',
#     'age': 23,
#     'email': 'dave@gmail.com',
#     'username': 'dave1234',
#     'student': True,
#     'class_completed': False,
# }
# # print(userdata['name'])
# for key, val in userdata.items():
#     # print(key, val)
#     # key, val = i
#     print(f'The key "{key}" has a value of "{val}"')
    # if key == 'email':
    #     print(f'Your email is {val}')

# userdata = {}
# userdata['name'] = input('What is your name? ')
# userdata['age'] = int(input('What is your age? '))
# print(userdata)


# highscores = [
#     {
#         'username': 'dave',
#         'score': 99
#     },
#     {
#         'username': 'jim',
#         'score': 85
#     }
# ]
# # for i in highscores:
# #     for key, val in i.items():
# #         print(key, val)
# print(highscores[0]['score'])

# num = [2, 4]
# num.append(6)
# num.append('Hello')
# num.append(True)
# num.append({'message': 'Good evening'})
# num.insert(1, 'I am first')
# print(num)

# for i in range(7):
#     entry = int(input('Type a number: '))
#     num.append(entry)
# num.insert(2, 6)
# del num[1]
# del num[0]
# del num[123456]
# print(num)


# userdata = []
#
# for i in range(3):
#     username = input('What is your username? ')
#     password = int(input('What is your password? '))
#     data = {
#         'username': username,
#         'password': password,
#     }
#     userdata.append(data)
# ic(userdata)


def userfunc():
    userdata = [{'password': 123, 'username': 'dave'},
                {'password': 456, 'username': 'mark'},
                {'password': 789, 'username': 'sally'}]
    
    for data in userdata:
        ic(data)

userfunc()
