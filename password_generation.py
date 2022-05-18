import random
import string
# 
def get_random_password():
    random_source = string.ascii_letters + string.digits + string.punctuation
   
    password = ""
# length of the range defines the length of the password 
    for i in range(10):
        password += random.choice(random_source)

    password_list = list(password)
    
    password = ''.join(password_list)
    return password

print("Password ", get_random_password())
