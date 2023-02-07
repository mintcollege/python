charlist = ['a', 'b', 'c']
student = [3621, 'Ramon', 'Communication']
student_dict = {
    'id': 3621,
    'name': 'Ramon',
    'course': 'Communication'
}
del student_dict['id']
# print(student_dict['id'])
# charlist.insert(0, 'd')
# del charlist[3]
# print(charlist)

# for idx, val in enumerate(charlist):
#     print(idx, val)

# for _, val in student_dict.items():
#     print(val)

# for i in range(3):
#     print(i)

base = int(input('Type in a positive integer: '))
for i in range(1, base + 1):
    ast = ''
    for j in range(i):
        ast += '*'
    print(ast)

# for i in range(1, base + 1):
#     ast = '*' * i
#     print(ast)