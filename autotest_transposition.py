import random
import sys

import transposition

random.seed('07092003')
for i in range(20):
    message = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40))
    random.shuffle(message)
    message = ''.join(message)
    print(f'Test {i+1}: {message[:20]}...', end='')
    for key in range(1, int(len(message) / 2)):
        encrypted = transposition.encrypt(message, key)
        decrypted = transposition.decrypt(encrypted, key)
        if message != decrypted:
            print('Missmatch', key, message)
            print('Decrypted as', decrypted)
            sys.exit()
    print(' ✔')
print('Tests have been passed')
