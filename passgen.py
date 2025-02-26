import string
import random

length = int(input('Enter the length of password: '))

characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(characters) for i in range(length))

print('Generated password: ' + password)