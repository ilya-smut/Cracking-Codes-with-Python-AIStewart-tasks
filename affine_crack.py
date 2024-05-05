import AffineCipher.affine_cipher
import AffineCipher.utils
import is_english

Af = AffineCipher.affine_cipher.AffineCipher()

ciphertext = Af.encrypt('This is the plaintext we are aiming at', Af.make_key_manually(17, 30))

for key in range(2, len(ciphertext)**2):
    decrypted = Af.decrypt(ciphertext, key)
    if is_english.is_english(decrypted):
        print(decrypted)



