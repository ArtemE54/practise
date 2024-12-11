def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""

    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - base - shift) % 26 + base)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char

    return decrypted_text


# Пример использования
ciphertext = "lvkdn"
shift = 3
decrypted_message = caesar_decrypt(ciphertext, shift)

print("Расшифрованное сообщение:", decrypted_message)
