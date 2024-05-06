import make_word_patterns
from make_word_patterns import get_word_pattern
import re, simple_substitution, copy

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
all_patterns = make_word_patterns.get_all_patterns('dictionary.txt')
non_letters_or_space_pattern = re.compile('[^A-Z ]')
"""
Regular expressions are strings that define a specific pattern that matches
certain strings.
Let's break down the pattern:
    []: Square brackets denote a character class, meaning any character inside these brackets will be matched.
    ^: Inside a character class, the caret symbol (^) negates the character class, meaning it matches any character not specified within the brackets.
    A-Z: This specifies a range of characters from A to Z, inclusive. So, any uppercase letter will be matched.
    ' ': This matches any whitespace character, such as space, tab, or newline.
"""


def blank_cipher_mapping():
    return {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [],
            'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [],
            'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [],
            'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []}


def main():
    message = ('Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr '
               'jia aqsoaxwa sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac ilxo, ia sr pyyacao '
               'rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu sx lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px '
               'jia rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh. -Facjclxo Ctrramm')
    print(crack_substitution(message))


def add_letters_to_mapping(mapping, cipherword, candidate):
    # This function adds the letters in the candidate as potential
    # decryption letters for the cipherletters in the cipherletter
    # mapping.
    for i in range(len(cipherword)):
        if candidate[i] not in mapping[cipherword[i]]:
            mapping[cipherword[i]].append(candidate[i])


def intersect_mappings(map_a, map_b):
    # To intersect two maps, create a blank map and then add only the
    # potential decryption letters if they exist in BOTH maps:
    intersected_mapping = blank_cipher_mapping()
    for letter in LETTERS:
        # An empty list means "any letter is possible". In this case just
        # copy the other map entirely:
        if not map_a[letter]:
            intersected_mapping[letter] = copy.deepcopy(map_b[letter])
        elif not map_b[letter]:
            intersected_mapping[letter] = copy.deepcopy(map_a[letter])
        else:
            # If a letter in mapA[letter] exists in mapB[letter],
            # add that letter to intersectedMapping[letter]:
            for mapped_letter in map_a[letter]:
                if mapped_letter in map_b[letter]:
                    intersected_mapping[letter].append(mapped_letter)
    return intersected_mapping


def remove_solved_letters_from_mapping(letter_mapping):
    # Cipherletters in the mapping that map to only one letter are
    # "solved" and can be removed from the other letters.
    # For example, if 'A' maps to potential letters ['M', 'N'], and 'B'
    # maps to ['N'], then we know that 'B' must map to 'N', so we can
    # remove 'N' from the list of what 'A' could map to. So 'A' then maps
    # to ['M']. Note that now that 'A' maps to only one letter, we can
    # remove 'M' from the list of letters for every other letter.
    # (This is why there is a loop that keeps reducing the map.)
    loop_again = True
    while loop_again:
        loop_again = False

        # solved_letters will be a list of uppercase letters that have one
        # and only one possible mapping in letter_mapping:
        solved_letters = []
        for cipherletter in LETTERS:
            if len(letter_mapping[cipherletter]) == 1:
                solved_letters.append(letter_mapping[cipherletter][0])

        # If a letter is solved, then it cannot possibly be a potential
        # decryption letter for a different ciphertext letter, so we
        # should remove it from those other lists:
        for cipherletter in LETTERS:
            for s in solved_letters:
                if len(letter_mapping[cipherletter]) != 1 and s in letter_mapping[cipherletter]:
                    letter_mapping[cipherletter].remove(s)
                    if len(letter_mapping[cipherletter]) == 1:
                        # A new letter is now solved
                        loop_again = True

    return letter_mapping


def get_ciphertext_mapping(message: str):
    intersected_map = blank_cipher_mapping()
    cipher_wordlist = non_letters_or_space_pattern.sub('', message.upper()).split()

    for cipher_word in cipher_wordlist:

        # Get a new cipherletter mapping for each ciphertext word:
        candidate_map = blank_cipher_mapping()
        pattern = get_word_pattern(cipher_word)

        if pattern not in all_patterns:
            continue

        # Add letters of each candidate to mapping
        for candidate in all_patterns[pattern]:
            add_letters_to_mapping(candidate_map, cipher_word, candidate)

        # Intersect the new mapping with the existing intersected mapping:
        intersected_map = intersect_mappings(intersected_map, candidate_map)

    # Remove any solved letters from the other lists:
    return remove_solved_letters_from_mapping(intersected_map)


def attempt_decryption_with_mapping(ciphertext, mapping):
    sub_key = ['x'] * len(LETTERS)
    for cipherletter in LETTERS:
        if len(mapping[cipherletter]) == 1:
            index_in_key = LETTERS.find(mapping[cipherletter][0])
            sub_key[index_in_key] = cipherletter
        else:
            ciphertext = ciphertext.replace(cipherletter.lower(), '_')
            ciphertext = ciphertext.replace(cipherletter.upper(), '_')
    sub_key = ''.join(sub_key)

    return simple_substitution.decrypt(ciphertext, sub_key)


def crack_substitution(ciphertext):
    mapping = get_ciphertext_mapping(ciphertext)
    return attempt_decryption_with_mapping(ciphertext, mapping)


if __name__ == '__main__':
    main()
