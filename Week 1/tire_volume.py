# author: Patrick O'Neill

import math

from datetime import date

today = date.today()

def calc_tire_volume(w,a,d): 
    #this function calculates the volume of a tire based on its width (w), aspect ratior(a), and diameter(d)
    v=(math.pi * (w**2*a*(w*a+2540*d)))/10000000000
    return v

def main():
    #this function asks the user for the width, aspect ratio and diameter of a tire and then calls the function
    #that calculates the tire volume based on those parameter, it then prints out the volume
    #This function also appends the data that user inputs along with the tire volume to a file called "volumes.txt"
    width = int(input('Enter the width of the tire in mm (ex. 205): '))
    ratio = int(input('Enter the aspect ratio of the tire  (ex. 60): '))
    diameter = int(input('Enter the diameter of the wheel in inches (ex. 15): '))
    v = calc_tire_volume(width,ratio,diameter)
    print(f'The approximate volume is {v:.2f} liters')
    purchase = ''
    while purchase.lower() != 'yes' and purchase.lower() != 'no':
        purchase = input('Would you like to buy tires with the demensions that you entered? ')
        if purchase.lower() == 'yes':
            name = input('Please enter name: ')
            phone_number = input('Please enter phone number: ')
            break
        elif purchase.lower() == 'no':
            print('Ok! Have a nice day!')
            name = 'N/A'
            phone_number = 'N/A'
            break
        else: 
            print('Not a valid opetion, please enter "yes" or "no"')
    with open('volumes.txt', 'a') as file:
        file.write('(Date),  (tire width), (apect ratio), (diameter), (customer name), (phone number)\n')
        file.write(f'{today}, {width}, {ratio}, {diameter}, {v:,.2f}, {name}, {phone_number} \n')

main()

