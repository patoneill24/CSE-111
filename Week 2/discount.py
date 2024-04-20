#Author: Patrick O'Neill 

from datetime import datetime

DISC_RATE = 0.10
SALES_TAX_RATE = 0.06 

print('Please add all your items and enter 0 when done:')
subtotal = 0
cost = 1

while cost != 0:
    cost = float(input('What is the cost of the item? $ '))

    if cost == 0:
        break

    qty = int(input('How many are you buying? '))

    subtotal += cost * qty

dt = datetime.now()
today = dt.weekday()

discount = False

if subtotal >= 50 and (today == 1 or today == 2):
    dis_amount = subtotal* DISC_RATE
    subtotal -= subtotal*DISC_RATE
    discount = True

end_total = subtotal + subtotal* SALES_TAX_RATE
sales_tax = subtotal* SALES_TAX_RATE


if discount == True:
    print(f'discount amount: ${dis_amount:,.2f}')

print(f'sales tax amount: ${sales_tax:,.2f}')
print(f'total: ${end_total:,.2f}')