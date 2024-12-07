plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    if char.isalpha():  
        char_code = ord(char)
        
        if char.islower():
            char_code = ord('a') + (char_code - ord('a') + 1) % 26
        elif char.isupper():
            char_code = ord('A') + (char_code - ord('A') + 1) % 26
        
        encrypted_char = chr(char_code)
    else:
        encrypted_char = char

    encrypted_text += encrypted_char

print("Plain text:", plain_text)
print("Encrypted text:", encrypted_text)