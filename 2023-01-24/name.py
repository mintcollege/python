# Ask the user for their first name
# Ask the last name
# Print out the fullname: Your fullname is ___ and you are __ yrs old.
# ___ your age 5 years from now is ____


def clean_name(name: str):
    return name.strip().capitalize()

firstname = input('What is your first name? ')
firstname = clean_name(firstname)

lastname = input('What is your last name? ')
lastname = clean_name(lastname)

# fullname = firstname + ' ' + lastname
# fullname = 'Your fullname is: {} {}'.format(firstname, lastname)
fullname = f'{firstname} {lastname}'            # '1212'

age = input('How old are you? ')
age = age.strip()

message = f'Your full name is {fullname} and you are {age} years old.'
futureage = int(age) + 5
message2 = f'{fullname} your age 5 years from now is {futureage}'
print(message2)

