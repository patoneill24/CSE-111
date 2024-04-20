# Get info from user
age = input('How old are you? ')
name = input('What is your name? ')
height = input('How tall are you in cats? ')

# Add that info to a file: 
with open('demo.log', 'a' ) as file:
    file.write(f'{name.capitalize()} is {age} years old and {height} cats tall.\n')
