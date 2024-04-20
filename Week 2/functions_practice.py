#positional

def foo(bar,baz):
    print(bar, baz)

foo('Hello', 'World')

#default values

def foo(bar,baz=42):
    print(bar,baz)

foo('Hello')

# *args

def family(surname, *names):
    for name in names:
        print(f'{name} {surname}')

family('Keers', 'Reyna', 'Chris', 'Matthew')

