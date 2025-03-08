import random 

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,123456790'

number = int(input("Enter your number: "))

length = int(input("Enter your password length: "))

print('\nhere are your password')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
        
print(passwords)