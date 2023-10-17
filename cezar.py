def caesar_cipher_russian(text, n):
    result = ""
    
    for char in text:
        if char.isalpha():
            # Определяем, является ли символ буквой
            if char.isupper():
                # Если символ в верхнем регистре
                result += chr(((ord(char) - ord('А') - n) % 26) + ord('А'))
            else:
                # Если символ в нижнем регистре
                result += chr(((ord(char) - ord('а') - n) % 26) + ord('а'))
        else:
            # Если символ не буква, оставляем его без изменений
            result += char
    
    return result


def caesar_decrypt(text, n):
    result = ""
    russian_alphabet = "АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" 
    
    for char in text:
        if char.isalpha():
            if char.isupper():
                # Если символ в верхнем регистре
                result += chr(((ord(char) - ord('А') + n) % 26) + ord('А'))
            else:
                # Если символ в нижнем регистре
                result += chr(((ord(char) - ord('а') + n) % 26) + ord('а'))
        else:
            # Если символ не буква, оставляем его без изменений
            result += char
    
    return result