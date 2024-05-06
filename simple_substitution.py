import random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def get_random_key():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)


def vrfy_key(key):
    if type(key) is str and len(key) == len(LETTERS):
        return True
    else:
        return False


def translate(message, key, mode='e'):
    if mode == 'e' and vrfy_key(key):
        original_chars, translation_chars = LETTERS, key
    elif mode == 'd' and vrfy_key(key):
        translation_chars, original_chars = LETTERS, key
    else:
        return None

    translated_message = ''
    for letter in message:
        if letter.upper() in original_chars:
            letter_index = original_chars.find(letter.upper())
            if letter.isupper():
                translated_message += translation_chars[letter_index]
            else:
                translated_message += translation_chars[letter_index].lower()
        else:
            translated_message += letter
    return translated_message


def encrypt(message, key):
    return translate(message, key, mode='e')


def decrypt(message, key):
    return translate(message, key, mode='d')


if __name__ == '__main__':
    key = get_random_key()
    print(key)
    message = 'Sample Message Nothing to See Here'
    print(message)
    encrypted = encrypt(message, key)
    print(encrypted)
    decrypted = decrypt(encrypted, key)
    print(decrypted)

