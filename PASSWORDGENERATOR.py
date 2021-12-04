#PASSWORDGENERATOR
#Filip Rokita
#www.filiprokita.com

import string
import random

special = "!@#$%^&*()-_=+"

def generate_password(password_length):
    characters = string.digits + string.ascii_lowercase + string.ascii_uppercase + special
    result = "".join(random.choice(characters) for i in range(password_length))
    return result

def check_password(input_password):
    has_digits = 0
    has_ascii_lowercase = 0
    has_ascii_uppercase = 0
    has_special = 0
    for i in range (len(input_password)):
        for j in range(len(string.digits)):
            if input_password[i] == string.digits[j]: has_digits = 1
        for j in range(len(string.ascii_lowercase)):
            if input_password[i] == string.ascii_lowercase[j]: has_ascii_lowercase = 1
        for j in range(len(string.ascii_uppercase)):
            if input_password[i] == string.ascii_uppercase[j]: has_ascii_uppercase = 1
        for j in range(len(special)):
            if input_password[i] == special[j]: has_special = 1
    score = has_digits + has_ascii_lowercase + has_ascii_uppercase + has_special
    if score == 4:
        return 1
    else:
        return 0

while True:
    length = int(input("LENGTH: "))
    if length >= 4:
        if length < 8:
            print("WARRNING: Passwords shorter than 8 characters are not secure!")
        break
    print("ERROR: Password cannot be shorter than 4 characters! Try again.")

while True:
    initial_password = generate_password(length)
    if check_password(initial_password) == 1:
        password = initial_password
        break;

print("PASSWORD:", password)