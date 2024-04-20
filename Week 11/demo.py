numbers = [7,5,8,24,42,37]

#def triple(num):
    #return num * 3

mod_numbers = list(map(lambda num: num * 3, numbers))

print(f'Original number: {numbers}')
print(f'modified_numbers: {mod_numbers}')

print()


# Filter

odd_nums = list(filter(lambda num: num % 2 == 1, numbers))
even_nums= list(filter(lambda num: num % 2 == 0, numbers))

print(f'Original numbers: {numbers}')
print(f'only even numbers: {even_nums}')
print(f'only odd numbers: {odd_nums}')