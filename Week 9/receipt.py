#Author: Patrick O'Neill

import csv

# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()
# gets the day of the week to figure out if it is tuesday or wendsday
# which will determine the if customer gets discount or not
today = current_date_and_time.weekday()
time= current_date_and_time.time()
# gets the current hour to figure out if it is before 11am which 
# will determine if customer gets discount or not
current_hour = time.hour

SALES_TAX = 0.06
DISCOUNT_RATE = 0.10

def main():
    """
    This function calls the read_dictionary file to produce a dictionary from the 
    products.csv file. From that dictionary, the request.csv file picks out 
    products the customer would like to buy along with the quantity of each product. 
    This function then uses the data in the dictionary to calculate 
    the costs of the items the customer requested and applies sales tax and discount to get 
    the final cost for the customer. Then there is error handling for two common errors that 
    could happen with this program. 
    """
    try:
        PRODUCTS_KEY = 0
        QUANTITY_KEY = 1
        PRODUCTS_NAME_KEY = 1
        PRODUCTS_PRICE_KEY = 2
        products_dict = read_dictionary('products.csv',PRODUCTS_KEY)
        print('Inkom Emporium')
        print()
        print('Requested Items: ')
        with open('request.csv', 'r') as request_file:
            reader= csv.reader(request_file)
            #skips first line because it is just the title
            next(reader)
            quantity_total = 0
            product_price_subtotal = 0
            for row_list in reader:
                # gets product key and quantity requestity to calculate costs for the reciept
                product = row_list[PRODUCTS_KEY]
                quantity = int(row_list[QUANTITY_KEY])
                # adds up the number of items being bought
                quantity_total += quantity
                # picks product from the products.csv file based on the product key
                # given in request.csv file
                # then procedes to get name of product and price
                value = products_dict[product]
                product_name = value[PRODUCTS_NAME_KEY]
                product_price = float(value[PRODUCTS_PRICE_KEY])
                # calculates price of product based on the price per item times
                # the number of items requested
                #then adds up costs to give subtotal
                total_price_of_product = product_price * quantity
                product_price_subtotal += total_price_of_product
                print(f'{product_name}: {quantity} @ {product_price}')
            #calcualtes sales tax and discount to give final total
            sales_tax_amount = product_price_subtotal * 0.06
            product_price_total = product_price_subtotal + sales_tax_amount
            discount = product_price_total * 0.10
            total_with_discount = product_price_total - discount
            print()  
            print(f'Number of items: {quantity_total}')
            print(f'Subtotal: {product_price_subtotal:.2f}')
            print(f'Sales tax: {sales_tax_amount:.2f}')
            print(f'Total: {product_price_total:.2f}')
            #If today is Tuesday or Wednsday or it's before 11am, there is a 10 percent discount 
            if today == 1 or today == 2 or current_hour < 11:
                print('10% off!')
                print(f'discount: {discount:.2f}')
                print(f'New total: {total_with_discount:.2f}')
            print()
            print('Thank you for shopping at Inkom Emporium!')
            # Use an f-string to print the current
            # day of the week and the current time and the date and year
            print(f"{current_date_and_time:%a %b %d %I:%M:%S %Y}")
    # how the program will handle a FileNotFoundError and KeyError
    except FileNotFoundError as file_err:
        print('Error: Missing file')
        print(file_err)
    except KeyError as error:
        print('Error: unknown product ID in the request.csv file')
        print(error)
        

                
def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
dictionary and return the dictionary
Parameters
    filename: the name of the CSV file to read.
    key_column_index: the index of the column
        to use as the keys in the dictionary.
Return: a compound dictionary that contains
    the contents of the CSV file.
"""
    dictionary = {}

    with open(filename, 'rt') as csv_file:
        reader= csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            key = row_list[key_column_index]
            dictionary[key] = row_list
    return dictionary


if __name__ == "__main__":
    main()