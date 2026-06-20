from random import choice

length_of_pass = 8
valid_chars_password = "qwertyuiop[]asdfghjkl;'zxcvbnm,./123456789!@~#$%^&*()_+-="

password = []
'''
for each in range(len(length_of_pass)):
    password.append(choice(valid_chars_password))

print("".join(password))
'''
randompass = "".join(choice(valid_chars_password)
                     for each in range(length_of_pass))
print(randompass)
