characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
key = 20
charset_len = len(characters)
message = 'This is my secret message.'


def encrypt(message, key):
    key = key % charset_len
    encrypted_string = ''
    for c in message:
        if c in characters:
            index = characters.find(c)
            enc_index = (index + key) % charset_len
            encrypted_string += characters[enc_index]
        else:
            encrypted_string += c
    return encrypted_string


def decrypt(ciphertext, key):
    key = key % charset_len
    decrypted_string = ''
    for c in ciphertext:
        if c in characters:
            index = characters.find(c)
            enc_index = (index - key) % charset_len
            decrypted_string += characters[enc_index]
        else:
            decrypted_string += c
    return decrypted_string

def bruteforce(ciphertext):
    for key in range(0,charset_len-1):
        print(decrypt(ciphertext, key))


if __name__ == '__main__':
    #ciphertext = encrypt(message, key)
    #decrypted = decrypt(ciphertext, key)
    #print(ciphertext)
    #print(decrypted)
    #print()
    ciphertext = 'ZqH8sl5HtqHTH4s3lyvH5zH5spH4t pHzqHlH3l5K'
    print(bruteforce(ciphertext))
