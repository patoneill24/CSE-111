# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime



def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input('Enter gender: (m/f)')
    birthdate = input('Enter birthdate: (YYYY-MM-DD)')
    height = float(input('Enter height in inches: '))
    weight = float(input('Enter weight in pounds: '))
    # Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.
    age = compute_age(birthdate)
    w_in_kg = kg_from_lb(weight)
    h_in_cm = cm_from_in(height)
    bmi = body_mass_index(w_in_kg, h_in_cm)
    bmr = basal_metabolic_rate(gender,w_in_kg,h_in_cm,age)


    # Print the results for the user to see.
    print(f'Age: {age}')
    print(f'Weight in kg: {w_in_kg:.2f}')
    print(f'height in cm: {h_in_cm:.1f}')
    print(f'Body Mass Index: {bmi:.1f}')
    print(f'Basal Metabolic Rate (kcal/day): {bmr:.0f}')
    pass


def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    w_in_kg = pounds * 0.45359237
    return w_in_kg


def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    h_in_cm = inches * 2.54
    return h_in_cm


def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    bmi = (10000*weight)/height ** 2
    return bmi 


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    bmr = 0
    if gender.lower == 'm':
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.667 * age
    else:
        bmr = 447.593 + 9.427 * weight + 3.098 * height - 4.330 * age
    return bmr

# Call the main function so that
main()
# this program will start executing.

