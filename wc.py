

def get_file(filename):
    try:
        file = open(filename, "r") #opens file with name of "alice30.txt"
        return file
    except Exception:
        print "sorry, no file existed with the name " + filename + " :("
        return None

if __name__ == '__main__':
    alice_in_wonderland = get_file("alice30.txt")
    if alice_in_wonderland:
        # print alice_in_wonderland.read()
        with alice_in_wonderland as f:
            for line in f:
                for word in line.split():
                    print word.strip(',.:-;?`!').lower()