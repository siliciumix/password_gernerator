import string
import random
import pyperclip

def generate_password(length=12, include_digits=True, include_special_chars=True, exclude_chars=True):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")
    
    characters = string.ascii_letters
    
    if exclude_chars:
        exclude_chars = 'il1Lo0O'
        characters = ''.join([c for c in characters if c not in exclude_chars])
    
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print()
print('Das folgende Password wurde in die Zwischenablage geschrieben: ')
print()
password = generate_password(length=16, include_digits=True, include_special_chars=True, exclude_chars=True)
pyperclip.copy(password)
print(password)
print()
