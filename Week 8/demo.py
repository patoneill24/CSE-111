FIRST_NAME = 0
LAST_NAME = 1
WAND_TYPE = 2

students = {
    "GG1": ["Godric","Griffindor", "Lion Hair Core Wand"],
    "SS1": ["Salazar", "Slytherin", "Snake Skin Wand"],
    "HP1": ["Helga", "Hufflepuff", "Pop Tart Wand"],
    "RC1": ["Towena", "Ravenclaw", "Bald Eagle Feather Wand"]
}

new_student = ["Tom", "Riddle", "Phoenix Feather Wand"]
students['VOLDY']= new_student

#for record in students:
    #student_id = record[0]
    #first_name = record[1][FIRST_NAME]
    #last_name = record[2][LAST_NAME]
    #wandtype = record[3][WAND_TYPE]

for student_id, record in students.items():
    first_name = record[FIRST_NAME]
    last_name = record[LAST_NAME]
    wandtype = record[WAND_TYPE]
    print(f'{first_name} {last_name} has a {wandtype}')