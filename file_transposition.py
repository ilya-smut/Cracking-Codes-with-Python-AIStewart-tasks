import os, sys, time, transposition

while True:
    input_file = input('Which txt file do you want to encrypt? > ')
    if os.path.exists(input_file) and input_file[-4:] == '.txt':
        break
    elif input_file[-4:] != '.txt':
        print('it is not txt file:', input_file)
        continue
    elif input_file == 'exit':
        sys.exit()
    else:
        print('No such file exists:', input_file)

output_file = input_file[:-4] + '.encrypted.txt'

if os.path.exists(output_file):
    print(output_file, 'will be overwritten. (C)ontinue or (Q)uit?')
    response = input()
    if not response.lower().startswith('c'):
        sys.exit()

key = int(input('Please, enter an integer key: '))

initial_time = time.time()
with open(input_file) as file:
    contents = file.read()

with open(output_file, 'w') as file:
    file.write(transposition.encrypt(contents, key))
print('Encryption successful in', time.time() - initial_time, 'seconds.')
