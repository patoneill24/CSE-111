# Author: Patrick O'Neill 

# t = 2pi sqrt h / 9.81

import math

pi = math.pi

def calc_pendulum_time(length):
    #calculates the time a pendulum swings

    # parameters: length (float): the height of the pendulum rope
    h = (2 * pi) * math.sqrt(length / 9.81)
    return h

def main():
    """
The time in seconds that a pendulum takes to swing back and
forth once is given by this formula:
             ____
            / h
    t = 2π / ----
          √  9.81

t is the time in seconds,
π is the constant PI, which is the ratio of the circumference
    of a circle divided by its diameter (use math.pi),
h is the length of the pendulum in meters.

Write a program that prompts a user to enter the length of a
pendulum in meters and then computes and prints the time in
seconds that it takes for that pendulum to swing back and forth.
"""
    h = float(input('Length of pendlum (meters): '))
    t = calc_pendulum_time(h)
    print(f'Time (seconds): {t:.2f}')

main()