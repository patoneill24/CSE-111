import csv

def main():
    ID_INDEX = 0
    NAME_INDEX = 1
    id_number = (input('Enter I-Number (xxx-xxxx-xx): '))
    student_dict = read_dictionary('/Users/patrickoneill/Documents/BYU-I/Fall-2023/CSE-111/Week 9/students.csv', ID_INDEX)
    x = id_number.replace('-','')
    if len(x) < 9:
        print('invalid I-Number, Too few digits')
    elif len(x) > 9:
        print('invalid I-Number, Too many digits')
    elif not x.isdigit():
        print('invalid I-Number, must only contain numbers')
    else:
        if x in student_dict:
            value = student_dict[x]
            name = value[NAME_INDEX]
            print(name)
        else: 
            print('No such student')


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}

    with open(filename, 'rt') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                dictionary[key] = row_list
    return dictionary



if __name__ == "__main__":
    main()




