import AffineCipher.affine_cipher
import AffineCipher.utils
import is_english

Af = AffineCipher.affine_cipher.AffineCipher()

ciphertext = Af.encrypt('This is the plaintext we are aiming at', Af.make_key_manually(17, 30))

'''
We know there are at most len(affineCipher.SYMBOLS) possible integers
for Key A and len(affineCipher.SYMBOLS) possible integers for Key B. To get
the entire range of possible keys, we multiply these values together. Because
we’re multiplying the same value by itself, we can use the ** operator in the
expression len(affineCipher.SYMBOLS) ** 2.
'''

for key in range(2, len(ciphertext)**2):
    decrypted = Af.decrypt(ciphertext, key)
    if is_english.is_english(decrypted):
        print(decrypted)



