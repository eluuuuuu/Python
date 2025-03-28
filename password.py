import random
import string

length_password = int(input("How long do you want your password to be? "))  # Convert input to integer

def password_protection(length):  # Define the function
    password = string.ascii_letters + string.digits + string.punctuation  # Combine letters, numbers, and symbols
    word = "".join(random.choices(password, k=length))  # Fix: add k=

    return word  # Return the generated password

print(password_protection(length_password))  # Call the function with the user's input
