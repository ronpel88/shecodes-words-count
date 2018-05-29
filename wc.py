def get_file(filename):
    try:
        file = open(filename, "r")  # opens file with name of "alice30.txt"
        return file, None
    except Exception:
        return None, "sorry, no file existed with the name " + filename + " :("


if __name__ == '__main__':
    file, msg = get_file("<file_path>")
    # if file existed
    if file:
        with file as f:
            for line in f:
                print line
    else:
        # if file not existed
        print msg
