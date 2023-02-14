# User creates a new item
# Marks as done
# Delete item

todolist = []
donelist = []


def create_item():
    """
    Adds a new todo item to the list
    """
    todoitem = input('Add an item: ')
    todolist.append(todoitem)

def delete_item():
    """
    Deletes an item from the list
    """
    index_str = input('Which item do you want to delete? ')
    index_int = int(index_str)
    del todolist[index_int]

def mark_done():
    """
    Marks an item as done
    """
    index_str = input('Mark which item as done? ')
    index_int = int(index_str)
    # add to donelist
    donelist.append(todolist[index_int])
    # remove from todolist
    del todolist[index_int]
        
def list_unfinished():
    """
    Print the entire unfinished list
    :return:
    """
    for idx, val in enumerate(todolist):
        print(f'{idx}: {val}')
    
def list_done():
    """
    Print all done items
    """
    for idx, val in enumerate(donelist):
        print(f'{idx}: {val}')


# create()
# create()
# # delete_item()
# mark_done()
#
# print(todolist)
# print(donelist)
# delete_item()
# print(todolist)


while True:
    action = input('Press /add to add, /delete to delete, /mark to mark, /todo to show items not yet done, '
                   'press Ctrl+C to exit: ')
    
    if action == '/add':
        create_item()
    elif action == '/delete':
        list_unfinished()
        delete_item()
    elif action == '/todo':
        list_unfinished()
    else:
        list_unfinished()
        mark_done()
        
    # add
    # delete
    # mark
