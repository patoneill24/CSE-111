file = open('filename.txt', 'r')
file.write('............\n')
file.close()


#new way: with open()
#you don't need to close the file with this new way  
with open('filename.txt', 'r') as file:
    for line in file:
        print(line)