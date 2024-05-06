def get_word_pattern(word):
    word = word.upper()
    letters_and_indexes = {}
    pattern = ''
    index = 0
    for letter in word:
        if letter not in letters_and_indexes:
            letters_and_indexes[letter] = index
            index += 1
        pattern += f'{str(letters_and_indexes[letter])}.'
    return pattern[:-1]
# returns a pattern like that '0.1.2.1.2.1' for BANANA


def get_wordlist(file):
    with open(file) as file:
        words = file.read().split('\n')
    return words


def get_all_patterns(file):
    all_patterns = {}
    wordlist = get_wordlist(file)
    for word in wordlist:
        pattern = get_word_pattern(word)
        if pattern not in all_patterns:
            all_patterns[pattern] = list()
            all_patterns[pattern].append(word)
        else:
            all_patterns[pattern].append(word)
    return all_patterns
# returns a dictionary like that {'0.1.2.3.4.1.2.5.6.5': ['WORKHORSES']}
