def get_file(filename):
    try:
        file = open(filename, "r")  # opens file with name of "alice30.txt"
        return file, None
    except Exception:
        return None, "sorry, no file existed with the name " + filename + " :("


if __name__ == '__main__':
    alice_in_wonderland, msg = get_file("alice30.txt")
    # if file existed
    if alice_in_wonderland:
        # print alice_in_wonderland.read()
        alice_wc_dictionary = {}
        with alice_in_wonderland as f:
            for line in f:
                for word in line.split():
                    formatted_word = word.strip(',.:-;?`!').lower()
                    # print formatted_word
                    if formatted_word in alice_wc_dictionary:
                        alice_wc_dictionary[formatted_word] += 1
                    else:
                        alice_wc_dictionary[formatted_word] = 0
        print alice_wc_dictionary
    else:
        # if file not existed
        print msg
