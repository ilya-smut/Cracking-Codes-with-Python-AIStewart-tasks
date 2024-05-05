from math import ceil

message = 'commonsense'
key = 5

target_ciphertext = """AaKoosoeDe5 b5sn ma reno ora'lhlrrceey e enlh
na indeit n uhoretrm au ieu v er Ne2 gmanw,forwnlbsya apor tE.no
euarisfatt e mealefedhsppmgAnlnoe(c -or)alat r lw o eb nglom,Ain
one dtes ilhetcdba. t tg eturmudg,tfl1e1 v nitiaicynhrCsaemie-sp
ncgHt nie cetrgmnoa yc r,ieaa toesa- e a0m82e1w shcnth ekh
gaecnpeutaaieetgn iodhso d ro hAe snrsfcegrt NCsLc b17m8aEheideikfr
aBercaeu thllnrshicwsg etriebruaisss d iorr."""
target_key = 6


def encrypt(message, key):
    ciphertext = ['']*key

    for column in range(key):
        current_index = column
        while current_index < len(message):
            ciphertext[column] += message[current_index]
            current_index += key

    return ''.join(ciphertext)


"""
To recap, the steps for decrypting are as follows:
1. Calculate the number of columns you need by dividing the length of
the message by the key and then rounding up.
2. Draw boxes in columns and rows. Use the number of columns you calculated
in step 1. The number of rows is the same as the key.
3. Calculate the number of boxes to shade in by taking the total number
of boxes (the number of rows multiplied by the number of columns)
and subtracting the length of the ciphertext message.
4. Shade in the number of boxes you calculated in step 3 at the bottom of
the rightmost column.
5. Fill in the characters of the ciphertext starting at the top row and going
from left to right. Skip any of the shaded boxes.
6. Get the plaintext by reading the leftmost column from top to bottom,
and continuing to do the same in each column.
"""


def decrypt(ciphertext, key):
    columns = ceil(len(ciphertext) / key)
    rows = key
    shaded_amount = columns*rows - len(ciphertext)
    plaintext = ['']*columns
    letter_index = 0
    for row in range(rows):
        for column in range(columns):
            if (column == columns-1) and row >= (rows - shaded_amount):
                continue
            else:
                plaintext[column] += ciphertext[letter_index]
                letter_index += 1

    return ''.join(plaintext)



