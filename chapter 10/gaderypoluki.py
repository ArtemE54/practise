def create_substitution_dict(key):
    # Создаем словарь подстановок
    substitution_dict = {}

    # Проходим по парам букв в ключе
    for i in range(0, len(key), 2):
        original = key[i]  # Первая буква пары
        substitute = key[i + 1]  # Вторая буква пары

        # Добавляем подстановки для прописных и строчных букв
        substitution_dict[original.upper()] = substitute.upper()
        substitution_dict[original.lower()] = substitute.lower()

        # Добавляем обратную подстановку
        substitution_dict[substitute.upper()] = original.upper()
        substitution_dict[substitute.lower()] = original.lower()

    return substitution_dict


def encode(message, key):
    substitution_dict = create_substitution_dict(key)
    encoded_message = ''.join(substitution_dict.get(char, char) for char in message)
    return encoded_message


def decode(encrypted_message, key):
    substitution_dict = create_substitution_dict(key)
    decoded_message = ''.join(substitution_dict.get(char, char) for char in encrypted_message)
    return decoded_message


# Примеры использования
print(encode("ABCD", "gaderypoluki"))  # => GBCE
print(encode("Ala has a cat", "gaderypoluki"))  # => Gug hgs g cgt
print(decode("Dkucr pu yhr ykbir", "politykarenu"))  # => Dance on the table
print(decode("Hmdr nge brres", "regulaminowy"))  # => Hide our beers
