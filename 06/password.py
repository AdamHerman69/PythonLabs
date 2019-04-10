import random
import string

def generate_password(length = 12, special_chars_count = 3):
    password = ""
    regular_chars = string.ascii_letters + "0123456789"
    special_chars = " !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    for i in range(length - special_chars_count):
        password += random.choice(regular_chars)
    for i in range(special_chars_count):
        index = random.randint(0, length - 1)
        password = password[:index] + random.choice(special_chars) + password[index:]
    return password
