#READ ME: This is a password generator.

import random
import string

#This function will generate the password.
def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters 
    if numbers:
        characters += digits 
    if special_characters:
        characters += special

    #Currently, this is the state of the password.
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    #We tell the machine to generate new characters from our random character list.
    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters) 
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        #define what conditions must be met in order for the password to meet the criteria.
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special
    
    return pwd

#Asks the users what parameters they would like for the password generator.
min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want to have numbers (y/n)? ").lower() == "y"
has_special = input("Do you want to have special character (y/n)? ").lower() == "y"
pwd = generate_password(min_length, has_number, has_special)
print("The generated password is: ", pwd)
