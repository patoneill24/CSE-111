def main():
    text_list = read_list('/Users/patrickoneill/Documents/BYU-I/Fall-2023/CSE-111/Week 9/provinces.txt')
    modify_list(text_list)
    print(text_list)
    count = text_list.count('Alberta')
    print(f'Alberta occurs {count} times in the modified list.')

def read_list(filename):
    text_list = []

    with open(filename, 'rt') as text_file:
        for line in text_file:
            clean_line = line.strip()
            text_list.append(clean_line)
    return text_list

def modify_list(list):
    for i in range(len(list)):
        if list[i] == 'AB':
            list[i] ='Alberta'
    last_item = len(list) - 1
    first_item = 0
    list.pop(last_item)
    list.pop(first_item)
    return list

#def alberta_counter(list):
    counter = 0
    for i in list:
        if 'Alberta' in i:
            counter += 1
    
    return counter

if __name__ == "__main__":
    main()

