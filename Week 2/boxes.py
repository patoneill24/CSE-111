#author: Patrick O'Neill 

import math


def boxes_needed(items,items_per_box):
    #this function divides the number of items by the number of items per box and then rounds up the answer to the highest whole number
    #the purpouse of this function is to give  us the amount of boxes needed to fit all the items. 
    number_of_boxes_needed = math.ceil(items/items_per_box)
    return number_of_boxes_needed

def main():
    #this function asks the user to input the number of items they have and the number of items that can go in each box
    #then this function calls the "boxes_needed" function so that the user can be told how many boxes are needed to box all of their items 
    number_of_items = int(input('Enter the number of items: '))
    number_of_items_per_box = int(input('Enter the number of items per box: '))
    number_boxes_needed = boxes_needed(number_of_items,number_of_items_per_box)
    print(f'For {number_of_items} items, packing {number_of_items_per_box} in each box, you will need {number_boxes_needed} boxes.')

main()

