#this asks the user for their age and converts it to an integer
age= int(input('What is your age? '))

#computs max heart rate 
max_heart_rate = 220 - age

#computes highest healthy heart rate 
higher_heart_rate = int(max_heart_rate * 0.85)

#computes lowest healthy heart rate 
lower_heart_rate = int(max_heart_rate * 0.65)

#prints statement of range of healthy heart rate based on age 
print(f'When you exercise to strengthen your heart, you should keep your heart rate between {lower_heart_rate} and {higher_heart_rate} beats per minute')