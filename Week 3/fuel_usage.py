#Author: Patrick O'Neill

"""
Write a Python program named fuel_usage.py that asks the user
for three numbers:
1. A starting odometer value in miles
2. An ending odometer value in miles
3. A amount of fuel in gallons

Your program must calculate and print fuel efficiency in both
miles per gallon and liters per 100 kilometers. Your program
must have three functions named as follows:
1. main
2. miles_per_gallon
3. lp100k_from_mpg

All user input and printing must be in the main function. In other
words, the miles_per_gallon and lp100k_from_mpg functions must not
call the the input or print functions.
"""

def miles_per_gallon(end,start,gallons):
    #calculates the miles per gallon by diving the amount of miles driven by the amount of gallons used
    mpg = abs(end-start)/gallons
    return mpg

def lp100k_from_mpg(mpg):
    #calculates the amount of liters of gas used for every 100 km
    liters = 235.215/mpg
    return liters

def main():
    #asks the user to input the ending and starting odometer reading and the amount of gallons used
    #then calls the miles_per_gallon function to calcualte the miles per gallon the car gets
    #after that calls the lp100 function to calculate the amount of liters used per 100k the car goes
    #the liters per 100km and miles per gallon values are then printed
    end = float(input('An ending odometer value in miles: '))
    start = float(input('A starting odometer value in miles: '))
    gallons = float(input('An amount of fuel in gallons: '))
    mpg = miles_per_gallon(end,start,gallons)
    lp100k = lp100k_from_mpg(mpg)
    print(f'{mpg:.1f} miles per gallon')
    print(f'{lp100k:.2f} liters per 100 kilometers')

#calls the main function
main()
