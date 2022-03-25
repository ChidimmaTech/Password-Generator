import string
import random
generator: list(string.ascii_letters + string.digits + "!@#$%^&*()")

print('Welcome to your password generator!\n')
length = int(input('Enter the length of password you want:\n'))
'''
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
'''
generator = string.ascii_letters + string.digits + "!@#$%^&*()"
password = "".join(random.sample(generator,length))










print('Here is your password:', password)
