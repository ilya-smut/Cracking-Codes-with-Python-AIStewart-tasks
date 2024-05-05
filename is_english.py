# Inspired by and adopted from Cracking Codes with Python AI Stewart

UPPER_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = set(UPPER_LETTERS + UPPER_LETTERS.lower() + ' \t\n')


def load_dictionary():
    english = set()
    with open('dictionary.txt') as file:
        for word in file.read().split('\n'):
            english.add(word)
    return english


ENGLISH_WORDS = load_dictionary()


def remove_non_letters(message):
    letters_only = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            letters_only.append(symbol)
    return ''.join(letters_only)


def get_english_count(message):
    possible_words = remove_non_letters(message).upper().split()
    if not possible_words:
        return 0.0

    matches = 0
    for word in possible_words:
        if word in ENGLISH_WORDS:
            matches += 1

    return float(matches) / len(possible_words)


def is_english(message, word_percentage=20, letter_percentage=85):
    # By default, 20% of the words must exist in the dictionary file, and
    # 85% of all the characters in the message must be letters or spaces
    # (not punctuation or numbers).
    if type(message) is not str:
        return False
    words_match = get_english_count(message) * 100 >= word_percentage
    letters_match = (len(remove_non_letters(message)) / len(message)) * 100 >= letter_percentage

    return words_match and letters_match
