import string
import random

small_alphabets = string.ascii_lowercase  # a - z
upper_alphabets = string.ascii_uppercase  # A - Z
special_characters = string.punctuation  # -+/?*
numbers = string.digits  # 0 - 9

types = [upper_alphabets, small_alphabets, special_characters, numbers]

password = []

# password_length = random.randint(8, 16)
password_length = 32

i = 0
while i <= password_length:
    for type in types:
        random_character = random.choice(type)
        password.append(random_character)
        i = i + 1

print(password_length)
random.shuffle(password)
print("".join(password))
