import string
import random

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

# Beispielaufruf
print()
for i in range(1,10):
    password = generate_password(length=16, include_digits=True, include_special_chars=True, exclude_chars=True)
    print(password)
print()