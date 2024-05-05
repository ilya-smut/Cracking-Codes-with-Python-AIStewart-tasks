import transposition, is_english

ciphertext = transposition.encrypt(
    """Augusta Ada King-Noel, Countess of Lovelace (10 December 1815 - 27 November
1852) was an English mathematician and writer, chiefly known for her work on
Charles Babbage's early mechanical general-purpose computer, the Analytical
Engine. Her notes on the engine include what is recognised as the first
algorithm intended to be carried out by a machine. As a result, she is often
regarded as the first computer programmer.""",
    6)


def brute_force(message):
    for key in range(1, len(message)):
        decrypted = transposition.decrypt(message, key)
        if is_english.is_english(decrypted):
            print(decrypted)



brute_force(ciphertext)
