# Copyright 2023, Brigham Young University-Idaho. All rights reserved. (Keers)

# This line and line 1 are single line comments.

"""
This is a multi-line comment in Python. Technically speaking multi-line comments
do not exist in python, we are taking advantage of the fact that Python will
ignore multi-line strings not assigned to a variable.

Every file should include a header comment, a multiline comment at the top of the
file, that explains the purpose of this file; usually a summary of what it does.
You can include copyright and warranty information in this comment or you can
place them in separate comments like the copyright statement one line 1.

When we get into classes you will include things like attributes and methods that
are exposed (available) for users to use (call).
"""

import math # This is an import which will be discussed later.

"""
================================================================================
Python variables of various datatypes.
================================================================================
"""

# Integers (int).
length = 5
x = 14
time = 7.2

# Floating Point (float)
sample = 7.51

# Boolean (bool). Notice this is case sensitive, you must capitalize the bool!
in_flight = True
found = True
not_found = False

# Strings (str)
first_name = "Cho"
greeting = "Hello"
text = "23"

# Lists (list); aka. an Array (ary) in other programming languages.
colors = ["yellow", "red", "green", "yellow", "blue"]
samples = [6.5, 7.2, 7.0, 8.1, 7.2, 6.8, 6.8]

# Dictionary (dict); aka an Object (obj) in other programming languages.
students = {
    "42-039-4736": "Clint Huish",
    "61-315-0160": "Amelia Davis",
    "10-450-1203": "Ana Soares",
    "75-421-2310": "Abdul Ali",
    "07-103-5621": "Amelia Davis"
}

"""
================================================================================
Converting Datatypes (Casting)
================================================================================
"""

# Learn more about casting at: https://www.w3schools.com/python/python_casting.asp

text_to_number = int(text)      # '23' becomes 23
text_to_float = float("3.14")   # '3.14' becomes 3.14

"""
================================================================================
Getting Input
================================================================================
"""

"""
NOTE: I ask for user input (str) and immediately cast it to a different datatype
(int). This is valid code but may be encouraged or discouraged based on the
coding practices of your workplace.
"""

fav_num = int(input("What is your favorite whole number? "))
name = input("Please enter your name: ")
color = input("What is your favorite color? ")
print() # Give space between the next demo.

"""
================================================================================
Using and Displaying Input
================================================================================
"""

# Old school string concatenation. DON'T DO THIS!
print("Hi " + name + "! Your favorite color is " + color + ".")

# New school, proper, string formatting.
print(f"Hi {name}! Your favorite color is {color}.")

"""
NOTE: I performed an operation inside the formatted string below by multiplying
your favorite number by 10. This is valid code but may be encouraged or
discouraged based on the coding practices of your workplace.
"""

print(f"{name} your favorite number ({fav_num}) times 10 is {fav_num * 10}!")
print() # Give space between the next demo.

"""
================================================================================
Advanced Display
================================================================================
"""

# We can, usually for debugging purposes, print a variables datatype information.

d = False  # boolean
e = True   # boolean
print(f"{type(d)} {d}")
print(f"{type(e)} {e}")
print() # Give space between the next demo.

f = 15     # int
g = 7.62   # float
h = f + g  # int plus float makes float
print(f"{type(f)} {f}")
print(f"{type(g)} {g}")
print(f"{type(h)} {h}\n") # NOTE: Added a newline character \n here.

long_msg = """
NOTE: There is an extra space between this print statement and the previous one
because I used an newline character [\\n] in the last print statement. If you are
reading this comment in the code file you will notice I had to use multiple
backslash characters with the [n] so the backslash would appear as a string and
not a new line (line break).\n
"""
print(long_msg)


"""
================================================================================
Import Libraries
================================================================================
"""

"""
You can import libraries into your Python scripts to add additional functionality
without having to code it from scratch. Imports should be added at the top of your
file before any actual code; they can be placed after header comments however.

Here are some examples of the `math` library:
"""

print(math.pi)
print(math.sqrt(math.pi))
print() # Give space between the next demo.

"""
================================================================================
Functions (NEW)
================================================================================
"""

"""
This is new material for CSE 111. This is how you declare (or define) a function
in Python. This is a simple function with its own docstring, aka. doc block or
header comment, that explains how to use it correctly.
"""

def do_simple_addition(x, y=0):
    """
    Adds two numbers

    Adds two numbers of any combination of int and/or float and returns the
    result to the user.

    Parameters:
    x (int|float): The first number for our addition equation.
    y [int|float, 0]: The second number for our addition equation.
  
    Returns:
    int|float: The result of adding x and y together.
    """
    return x + y

do_simple_addition(x)

print(f"Did you know that 100 plus -50 is {do_simple_addition(100, -50)}?")

"""
NOTE: This function assumes that you will ALWAYS pass in proper values: int or
float. It also does not perform any type of error handling in case bad values
were passed in. You will also notice that we can provide negative numbers.
"""