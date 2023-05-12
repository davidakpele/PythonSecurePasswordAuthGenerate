import random
import string

def generate_password(genpassword):
    # Generate a random string of lowercase letters, uppercase letters, and digits
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(15))

    # Add a prefix based on the genpassword
    prefix = genpassword[:3].lower()
    password = prefix + password

    return password


# Get username from user
genpassword = input("Enter your password: ")

# Generate and print the password
# First Generated and printed password
password = generate_password(genpassword)
print("First Generated Password:", password)

# Second Generated and printed password
password = generate_password(genpassword)
print("Second Generated Password:", password)

# Third Generated and printed password
password = generate_password(genpassword)
print("Third Generated Password:", password)