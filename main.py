import string
import secrets


'''
Start define by user
'''
pass_len = 8
min_one_uppercase = True
min_one_digit = True
min_one_punct = True

'''
End define by user
'''

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
all_characters = letters + digits + special_chars

password = ''
password_ok = True
for i in range(pass_len):
    password += secrets.choice(all_characters)

if min_one_uppercase:
    if not any([el.isupper() for el in password]):
        #print("One upper exists")
        password_ok = False



if min_one_digit:
    if any([el.isdigit() for el in password]):
        #print("One digit")
        password_ok = False

if min_one_punct:
    if any([el in string.punctuation for el in password]):
        #print("One punctuation")
        password_ok = False

if password_ok == True:
    print(password)
else:
    print("Wrong password")
    print(password)

